#include <stdio.h>
#include "csapp.h"

/* Recommended max cache and object sizes */
#define MAX_CACHE_SIZE 1049000
#define MAX_OBJECT_SIZE 102400

void echo(int connfd);
int hostinfo(char *uri, char *ip_buf);
int getinfo(char *uri_ip, char *port, char *content);
void parse_uri(char *uri,char *hostname,char *path,int *port);


/* You won't lose style points for including this long line in your code */
static const char *user_agent_hdr =
    "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:10.0.3) Gecko/20120305 "
    "Firefox/10.0.3\r\n";

int main(int argc, char **argv)
{
  int listenfd, connfd;
  socklen_t clientlen;
  struct sockaddr_storage clientaddr;
  char hostname[MAXLINE], port[MAXLINE];

  if (argc != 2)
  { // 프록시서버 포트번호 설정
    fprintf(stderr, "usage : %s <port>\n", argv[0]);
    exit(0);
  }

  listenfd = Open_listenfd(argv[1]); // 서버를 연다(~listen)
  while (1)
  {
    clientlen = sizeof(clientaddr);
    connfd = Accept(listenfd, (SA *)&clientaddr, &clientlen);
    Getnameinfo((SA *)&clientaddr, clientlen, hostname, MAXLINE, port, MAXLINE, 0);
    printf("Accepted connection from (%s, %s)\n", hostname, port);
    echo(connfd);
    Close(connfd);
  }

  return 0;
}

void echo(int connfd)
{
  char buf[MAXLINE], method[MAXLINE], uri[MAXLINE], version[MAXLINE];

  /* 주소 */
  char hostname[MAXLINE], path[MAXLINE];
  int port;

  char http_header[MAXLINE];

  char *content;
  rio_t rio;
  content = (char *)Malloc(MAX_OBJECT_SIZE);

  printf("=========  echo part    =========\n");
  /* Read request line and headers */
  Rio_readinitb(&rio, connfd);
  Rio_readlineb(&rio, buf, MAXLINE);
  // printf("%s", buf);
  printf("Request headers:\n");
  // printf("%s", buf);
  sscanf(buf, "%s %s %s", method, uri, version);
  printf("=========  middle echo part    =========\n");
  printf("%s %s %s====\n", method, uri, version);
  // GET method만 받기, head는 나중에 구현
  // 포트는 이전에 port-for-user.pl로 다른 포트로 바꿔줘야함 -> 필요없음

  // hostinfo(uri, ip_buf);
  // printf("%s\n", ip_buf);

  parse_uri(uri, hostname, path, &port);



  /*build the http header which will send to the end server*/
  build_http_header(http_header,hostname,path,port,&rio);

  /*connect to the end server*/
  // end_serverfd = connect_endServer(hostname,port,http_header);
  // if(end_serverfd<0){
  //     printf("connection failed\n");
  //     return;
  // }

  // Rio_readinitb(&server_rio,end_serverfd);

  /*write the http header to endserver*/
  Rio_writen(end_serverfd,http_header,strlen(http_header));

  /*receive message from end server and send to the client*/
  char cachebuf[MAX_OBJECT_SIZE];
  int sizebuf = 0;
  size_t n;
  while((n=Rio_readlineb(&server_rio,buf,MAXLINE))!=0)
  {
      sizebuf+=n;
      if(sizebuf < MAX_OBJECT_SIZE)  strcat(cachebuf,buf);
      Rio_writen(connfd,buf,n);
  }

  Close(end_serverfd);

  /*store it*/
  if(sizebuf < MAX_OBJECT_SIZE){
      cache_uri(url_store,cachebuf);
  }

  printf("=========  end echo part    =========\n");

}




int hostinfo(char *uri, char *ip_buf)
{
  struct addrinfo *p, *listp, hints;

  int rc, flags;

  /* Get a list of addrinfo records */
  memset(&hints, 0, sizeof(struct addrinfo));
  hints.ai_family = AF_INET;       /* IPv4 only */
  hints.ai_socktype = SOCK_STREAM; /* Connections only */
  if ((rc = getaddrinfo(uri, NULL, &hints, &listp)) != 0)
  {
    fprintf(stderr, "getaddrinfo error: %s\n", gai_strerror(rc));
    return 1;
  }

  /* Walk the lsit and display each IP address */
  flags = NI_NUMERICHOST; /* Display address string instead of domain name */
  Getnameinfo(listp->ai_addr, listp->ai_addrlen, ip_buf, MAXLINE, NULL, 0, flags);

  /* Clean up */
  Freeaddrinfo(listp);
  return 0;
}

// int getinfo(uri_ip, 80, "GET", content)
int getinfo(char *uri_ip, char *port, char *content)
{
  int clientfd;
  char buf[MAXLINE];
  rio_t rio;

  clientfd = Open_clientfd(uri_ip, port);
  Rio_readinitb(&rio, clientfd);

  printf("=========  getinfo part    =========\n");

  /* make send message */
  sprintf(buf, "GET / HTTP/1.0\r\n");
  sprintf(buf, "%sHost: %s:%d\r\n", buf, uri_ip, port); 
  sprintf(buf, "%s%s\r\n", buf, user_agent_hdr); 
  sprintf(buf, "%sConnection: close", buf);
  sprintf(buf, "%sProxy-Connection: close", buf);
  sprintf(buf, "%sabc: 123", buf);

  printf("=========  getinfo middle    =========\n");

  Rio_writen(clientfd, buf, strlen(buf));

  Rio_readlineb(&rio, buf, MAXLINE);
  while(strcmp(buf, "\r\n"))
  {
    Rio_readlineb(&rio, buf, MAXLINE);
    sscanf(content, "%s%s", content, buf);
    printf("%s", buf); 
  }

  close(clientfd);
  printf("=========  getinfo end    =========\n");
  return 0;
}

void parse_uri(char *uri,char *hostname,char *path,int *port)
{
    *port = 80;
    char* pos = strstr(uri,"//");

    pos = pos!=NULL? pos+2:uri;

    char*pos2 = strstr(pos,":");
    if(pos2!=NULL)
    {
        *pos2 = '\0';
        sscanf(pos,"%s",hostname);
        sscanf(pos2+1,"%d%s",port,path);
    }
    else
    {
        pos2 = strstr(pos,"/");
        if(pos2!=NULL)
        {
            *pos2 = '\0';
            sscanf(pos,"%s",hostname);
            *pos2 = '/';
            sscanf(pos2,"%s",path);
        }
        else
        {
            sscanf(pos,"%s",hostname);
        }
    }
    return;
}