function addChange(editor, from, to, text) {
  let adjust = editor.listSelections().findIndex(({ anchor, head }) => {
    return CodeMirror.cmpPos(anchor, head) == 0 && CodeMirror.cmpPos(anchor, from) == 0;
  });
  editor.operation(() => {
    editor.replaceRange(text, from, to, 'yorkie');
    if (adjust > -1) {
      let range = editor.listSelections()[adjust];
      if (range && CodeMirror.cmpPos(range.head, CodeMirror.changeEnd({ from, to, text })) == 0) {
        let ranges = editor.listSelections().slice();
        ranges[adjust] = { anchor: from, head: from };
        editor.setSelections(ranges);
      }
    }
  });
}

async function main() {
  console.log("hit");
  const editor = CodeMirror.fromTextArea(
    document.getElementById("codemirror"),
    {
      lineNumbers: true,
    }
  );
  const client = new yorkie.Client("http://localhost:8080");
  await client.activate();

  // Document: 응용프로그램의 모델이 표현되는 CRDT 기반 데이터 유형. 
  // 클라이언트는 오프라인 상태에서도 편집할 수 있다.
  const doc = new yorkie.Document("docs", "doc1");
  await client.attach(doc);

  doc.update((root) => {
    if (!root.content) {
      root.content = new yorkie.Text();
    }
  });

  // (1) CodeMirror handler
  // Handler: 특정 유형의 데이터에 특화되어 있거나 특정 특수 작업에 초점을 맞춘 루틴/기능/태그
  editor.on("beforeChange", (cm, change) => {
    // (1) yorkie나 setValue라는 이름으로 변경이 일어날 때도 필터링
    if (change.origin === "yorkie" || change.origin === "setValue") {
      return;
    }
    console.log(change);
    // (2) CodeMirror에서 사용하는 Pos라는 타입이 있는데 커서의 위치 같은 것을 나타낸다.
    // 이것을 숫자 인덱스를 바꿔야 한다 → indexFromPos를 사용해서 변경
    const from = editor.indexFromPos(change.from);
    const to = editor.indexFromPos(change.to);
    // (3) CodeMirror에서 Text가 여러 줄일 때 배열로 와서 처리를 해야 한다.
    const content = change.text.join("\n");
    // (4) Yorkie Document를 업데이트
    doc.update((root) => {
      root.content.edit(from, to, content);
    });
  });
  // (2) Yorkie handler
  doc.getRoot().content.text.onChanges((changes) => {
    // (1) changes가 배열로 오기 때문에 반복문을 만든다.
    for (const change of changes) {
      console.log(changes);
      // (2) 자신의 편집을 반영할 필요는 없으니 본인을 필터하고 컨텐츠 변경이 아닌 경우 필터링
      if (change.type !== "content" || change.actor === client.getID()) {
        continue;
      }
      // (3) Pos를 index로 바꿨는데 이번엔 index를 Pos로 바꿔야 한다.
      const from = editor.posFromIndex(change.from);
      const to = editor.posFromIndex(change.to);
      // (4), (5)
      addChange(editor, from, to, change.content || '');
      // CodeMirror에서는 replaceRange라는 것으로 스크립트로 변경사항을 넣어줄 수 있다.
      // CodeMirror의 replaceRange가 원격 편집을 고려하지 않은 경우
      // editor.replaceRange(change.content, from, to, 'yorkie')
    }
  });
  // CodeMirror에서 제공하는 메소드를 호출해 초기값을 넣어준다.
  editor.setValue(doc.getRoot().content.toString());
}
main();
