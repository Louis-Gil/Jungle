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

  const doc = new yorkie.Document("docs", "doc1");
  await client.attach(doc);

  doc.update((root) => {
    if (!root.content) {
      root.content = new yorkie.Text();
    }
  });

  // (1) CodeMirror
  editor.on("beforeChange", (cm, change) => {
    // (1)
    if (change.origin === "yorkie" || change.origin === "setValue") {
      return;
    }
    console.log(change);
    // (2)
    const from = editor.indexFromPos(change.from);
    const to = editor.indexFromPos(change.to);
    // (3)
    const content = change.text.join("\n");
    // (4)
    doc.update((root) => {
      root.content.edit(from, to, content);
    });
  });
  // (2) Yorkie
  doc.getRoot().content.text.onChanges((changes) => {
    console.log(changes);
  });
}
main();
