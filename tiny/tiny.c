/* $begin tinymain */
/*
 * tiny.c - A simple, iterative HTTP/1.0 Web server that uses the
 *     GET method to serve static and dynamic content.
 *
 * Updated 11/2019 droh
 *   - Fixed sprintf() aliasing issue in serve_static(), and clienterror().
 */

#include "csapp.h"
#include <stdlib.h>

void doit(int fd);                                                       // 한개의 http 트랜잭션을 처리하는 함수
void read_requesthdrs(rio_t *rp);                                        // 요청 헤더 내의 정보를 읽고 무시하는 함수
int parse_uri(char *uri, char *filename, char *cgiargs);                 // 정적콘텐츠인지 동적콘텐츠인지 구분하여 맞게 처리하는 함수
void serve_static(int fd, char *filename, int filesize, char *method);   // 서버에서 정적콘텐츠를 처리해주는 함수
void get_filetype(char *filename, char *filetype);                       // 도메인을 받으면 분석해서 파일의 타입을 인지해서 정의해주는 함수
void serve_dynamic(int fd, char *filename, char *cgiargs, char *method); //서버에서 동적콘텐츠를 처리해주는 함수
void clienterror(int fd, char *cause, char *errnum, char *shortmsg,
                 char *longmsg); //상황에 맞는 에러메시지를 출력해주는 함수

// argc : arguments count (디폴트가 1)
// argv : arguments vector

int main(int argc, char **argv) //투포인터인 이유
{
  int listenfd, connfd;                  //서버에서 만드는 소켓
  char hostname[MAXLINE], port[MAXLINE]; // 주소/IP, port
  socklen_t clientlen;                   // 클라이언트의 ip = 32비트
  struct sockaddr_storage clientaddr;    //클라이언트소켓주소

  /* Check command line args */
  // 정상적인 주소 및 포트입력이 아니라면 (한개만 입력)
  if (argc != 2)
  {
    fprintf(stderr, "usage: %s <port>\n", argv[0]); // error메시지를 저장한다음에 출력하고 종료
    exit(1);
  }

  listenfd = Open_listenfd(argv[1]); // 듣기식별자 생성
  while (1)
  {
    clientlen = sizeof(clientaddr);              //클라이언트주소 크기
    connfd = Accept(listenfd, (SA *)&clientaddr, //클라이언트의 연결을 기다리고 받아주는 것 -> 연결식별자가 리턴( 0보다 크거나 같음 ) / -1 출력되면 에러
                    &clientlen);                 // line:netp:tiny:accept
    Getnameinfo((SA *)&clientaddr, clientlen, hostname, MAXLINE, port, MAXLINE,
                0);                                                // 리턴값이 0 / 잘 안 되면 에러코드
    printf("Accepted connection from (%s, %s)\n", hostname, port); // 클라이언트 Ip와 port 출력
    doit(connfd);                                                  // line:netp:tiny:doit
    Close(connfd);                                                 // line:netp:tiny:close
  }
}

void doit(int fd)
{
  int is_static;                                                      // 정적콘텐츠인지, 동적콘텐츠인지 알려주는 변수 ( is_static이 1이라면 정적콘텐츠 / 0이라면 동적콘텐츠)
  struct stat sbuf;                                                   // 소켓버프 (임시저장변수)
  char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE]; //예를 들어 uri는 파일이름과 인자, 버젼은 http 1.0 / 1.1
  char filename[MAXLINE], cgiargs[MAXLINE];                           // cgi인자는 ?뒤에 나오는 것으로 &로 구분
  rio_t rio;

  /* Read request line and headers */
  Rio_readinitb(&rio, fd);           // connectfd와 rio버퍼를 연결해주고 fd에 있는 값들을 전달해준다
  Rio_readlineb(&rio, buf, MAXLINE); // rio버퍼에 있는 것을 buf에다가 복사해준다.
  printf("Request headers:\n");
  printf("%s", buf); // buf에는 method, uri, version이 띄어쓰기로 나열되어 있다!!!

  sscanf(buf, "%s %s %s", method, uri, version); // method / uri / version 정의 완료

  if (strcasecmp(method, "GET") && strcasecmp(method, "HEAD")) // 인자 1과 인자2가 같으면 0을 출력합니다!
  {
    clienterror(fd, method, "501", "Not implemented", "Tiny does not implement this method");
    return;
  }

  /* parse URI from GET request */
  read_requesthdrs(&rio);

  is_static = parse_uri(uri, filename, cgiargs); // is_static이 1이면 정적 콘텐츠, 0이면 동적 콘텐츠
  if (stat(filename, &sbuf) < 0)                 // file의 정보를 가져와서 sbuf에 넣어주는 함수 (stat) / 0보다 작다는 것은 파일이 없다.
  {
    clienterror(fd, filename, "404", "Not found", "Tiny couldn't find this file");
    return;
  }

  /* Serve static content */
  if (is_static) // is_static 정적 콘텐츠라면,
  {
    if (!(S_ISREG(sbuf.st_mode)) || !(S_IRUSR & sbuf.st_mode)) // 일반파일이거나, 읽기권한을 가져야하는데, 둘 중에 하나라도 없으면 에러를 띄우겠습니다!
    {
      clienterror(fd, filename, "403", "Forbidden", "Tiny couldn't read the file");
      return;
    }
    serve_static(fd, filename, sbuf.st_size, method);
  }
  /* Serve dynamic content */
  else // 동적콘텐츠라면 동적 콘텐츠를 제공한다.
  {
    if (!(S_ISREG(sbuf.st_mode)) || !(S_IXUSR & sbuf.st_mode)) // 일반파일이거나, 실행권한을 가져야하는데, 둘 중 하나라도 없으면 에러
    {
      clienterror(fd, filename, "403", "Forbidden", "Tiny couldn't run the CGI program");
      return;
    }
    serve_dynamic(fd, filename, cgiargs, method);
  }
}

void clienterror(int fd, char *cause, char *errnum, char *shortmsg, char *longmsg)
{
  char buf[MAXLINE], body[MAXBUF];

  /* Build the HTTP response body */
  sprintf(body, "<html><title>Tiny Error</title>");
  sprintf(body, "%s<body bgcolor="
                "ffffff"
                ">\r\n",
          body);
  sprintf(body, "%s%s: %s\r\n", body, errnum, shortmsg);
  sprintf(body, "%s<p>%s: %s\r\n", body, longmsg, cause);
  sprintf(body, "%s<hr><em>The Tiny Web server</em>\r\n", body);

  /* Print the HTTP response */
  sprintf(buf, "HTTP/1.0 %s %s\r\n", errnum, shortmsg);
  Rio_writen(fd, buf, strlen(buf));
  sprintf(buf, "Content-type: text/html\r\n");
  Rio_writen(fd, buf, strlen(buf));
  sprintf(buf, "Content-length: %d\r\n\r\n", (int)strlen(body));
  Rio_writen(fd, buf, strlen(buf));
  Rio_writen(fd, body, strlen(body));
}

void read_requesthdrs(rio_t *rp)
{
  char buf[MAXLINE];

  Rio_readlineb(rp, buf, MAXLINE); // rp에서 텍스트를 읽고 buf로 복사
  printf("%s", buf);

  while (strcmp(buf, "\r\n"))
  {
    Rio_readlineb(rp, buf, MAXLINE);
    printf("%s", buf);
  }
  return;
}

int parse_uri(char *uri, char *filename, char *cgiargs) // 분석해서 동적인지, 정적인지 분류해주는 함수
{
  char *ptr;

  /* Static content */
  if (!strstr(uri, "cgi-bin")) // uri 내에 cgi-bin이 있는지 본다 -> 없다면 정적콘텐츠
  {
    strcpy(cgiargs, "");             // 인자를 ""초기화
    strcpy(filename, ".");           // filename도 "" 초기화
    strcat(filename, uri);           // filename에 uri를 붙여넣기 -> .~~~
    if (uri[strlen(uri) - 1] == '/') // uri의 맨 마지막이 /이면, home.html을 붙여준다.
      strcat(filename, "home.html");
    return 1;
  }
  else // 동적콘텐츠라면,
  {
    ptr = index(uri, '?'); // uri 내에 ?가 어디인지 찾아서 포인터를 반환
    if (ptr)               // ?가 있다면 -> ptr 존재
    {
      strcpy(cgiargs, ptr + 1); // ? 다음부분들을 인자에다가 덮어쓰기 해줍니다.
      *ptr = '\0';              // ?를 null로 바꿔준다.
    }
    else                   //?가 없다면 -> ptr 존재 안 한다면,
      strcpy(cgiargs, ""); // 인자가 없다는 소리이므로 그냥 ""해준다.
    strcpy(filename, "."); // filename에 .으로 덮어쓰기 하고
    strcat(filename, uri); // 뒤에 uri를 붙여준다.
    return 0;
  }
}

void serve_static(int fd, char *filename, int filesize, char *method) // 정적 콘텐츠를 제공하는 함수
{
  int srcfd;
  char *srcp, filetype[MAXLINE], buf[MAXBUF];

  /* Send response headers to client */
  get_filetype(filename, filetype);
  sprintf(buf, "HTTP/1.0 200 OK\r\n");
  sprintf(buf, "%sServer: Tiny Web Server\r\n", buf);
  sprintf(buf, "%sConnection: close\r\n", buf);
  sprintf(buf, "%sContent-length %d\r\n", buf, filesize);
  sprintf(buf, "%sContent-type: %s\r\n\r\n", buf, filetype);
  Rio_writen(fd, buf, strlen(buf)); // buf 에서 식별자 fd로 전송 /웹페이지에서 띄워지고
  printf("Response headers:\n");
  printf("%s", buf); // 터미널에서 출력

  if (strcasecmp(method, "HEAD") == 0)
    return;

  /* Send response body to client */
  srcfd = Open(filename, O_RDONLY, 0);                        //파일을 열고 성공시 파일식별자를 반환한다. (읽기 전용)
  srcp = Mmap(0, filesize, PROT_READ, MAP_PRIVATE, srcfd, 0); // 0 -> srcp 처음부터 붙여넣기해라, srcp 포인터에서부터 쭉 파일데이터를 복사합니다!!!!!, 0 -> 파일의 처음부터 복사해라!
  Close(srcfd);                                               // 파일식별자를 닫아버린다
  Rio_writen(fd, srcp, filesize);                             // srcp 에서 fd로 전송
  Munmap(srcp, filesize);                                     // free를 해준다.

  /* Send response body to client */
  // srcfd = Open(filename, O_RDONLY, 0);
  // srcp = (char *)malloc(sizeof(char) * filesize);
  // Rio_readn(srcfd, srcp, filesize);
  // Close(srcfd);
  // Rio_writen(fd, srcp, filesize);
  // free(srcp);
}
/*
 * get_filetype - Derive file type from filename
 */

void get_filetype(char *filename, char *filetype)
{
  if (strstr(filename, ".html"))
    strcpy(filetype, "text/html");
  else if (strstr(filename, ".gif"))
    strcpy(filetype, "image/gif");
  else if (strstr(filename, ".png"))
    strcpy(filetype, "image/png");
  else if (strstr(filename, ".jpg"))
    strcpy(filetype, "image/jpeg");
  else if (strstr(filename, ".mpg"))
    strcpy(filetype, "image/mpg");
  else
    strcpy(filetype, "text/plain");
}

void serve_dynamic(int fd, char *filename, char *cgiargs, char *method)
{
  char buf[MAXLINE], *emptylist[] = {NULL};

  /* Return first part of HTTP response */
  sprintf(buf, "HTTP/1.0 200 OK\r\n");
  Rio_writen(fd, buf, strlen(buf));
  sprintf(buf, "Server: Tiny Web Server\r\n");
  Rio_writen(fd, buf, strlen(buf));

  /*Child*/
  /* Real server would set all CGI vars here */
  if (Fork() == 0)
  {
    setenv("QUERY_STRING", cgiargs, 1);  // 환경변수를 변경 : QUERY_STRING / cgiargs
    setenv("REQUEST_METHOD", method, 1); // 환경변수를 변경 : QUERY_STRING / cgiargs

    Dup2(fd, STDOUT_FILENO);              /* Redirect stdout to client */
    Execve(filename, emptylist, environ); /* Run CGI program */
  }
  Wait(NULL); /* Parent waits for and reaps child */
}