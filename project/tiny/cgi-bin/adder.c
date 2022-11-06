#include "csapp.h"

int main(void)
{
    char *buf, *p, *method;
    char arg1[MAXLINE], arg2[MAXLINE], content[MAXLINE];
    int n1 = 0, n2 = 0;

    /* Extract the two arguments */
    if ((buf = getenv("QUERY_STRING")) != NULL)
    {
        p = strchr(buf, '&');
        *p = '\0';
        strcpy(arg1, buf + 6);
        strcpy(arg2, p + 7);
        n1 = atoi(arg1);
        n2 = atoi(arg2);
        // n1 = arg1;
        // n2 = arg2;
    }

    method = getenv("REQUEST_METHOD");
    printf("%s", method);
    if (!strcasecmp(method, "HEAD"))
    {
        sprintf(content, "HTTP/1.0 200 OK\r\n");
        sprintf(content, "%sServer: Tiny Web Server\r\n", content);
        sprintf(content, "%sConnection: close\r\n", content);
        sprintf(content, "%sContent-length: %d\r\n", content, strlen(content));
        sprintf(content, "%sContent-type: text/html\r\n\r\n", content);
        printf("Response headers:\n");
        printf("%s", content);

        fflush(stdout);

        exit(0);
    }

    /* Make the response body */
    sprintf(content, "QUERY_STRING=%s", buf);
    sprintf(content, "Welcome to add.com: ");
    sprintf(content, "%sTHE Internet addition portal. \r\n<p>", content);
    sprintf(content, "%sThe answer is: %d + %d = %d\r\n<p>",
            content, n1, n2, n1 + n2);
    sprintf(content, "%sThanks for visiting! \r\n", content);

    /* Generate the HTTP response */
    printf("Connection : close\r\n");
    printf("Content-length: %d\r\n", (int)strlen(content));
    printf("Content-type : text/html \r\n\r\n");
    printf("%s", content);

    fflush(stdout);

    exit(0);
}