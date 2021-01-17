/*
	Simple udp client
*/
#include<stdio.h>	//printf
#include<string.h> //memset
#include<stdlib.h> //exit(0);
#include<arpa/inet.h>
#include<sys/socket.h>

#define SERVER "127.0.0.1"
#define BUFLEN 512	//Max length of buffer
#define PORT 8888	//The port on which to send data


#define MSGLEN 1024

int main(void)
{





       int sockfd;
    FILE* fp;
    struct sockaddr_in sevrAddr;
    struct hostent *host;
    char readBuff[MSGLEN];
    int len;







































	struct sockaddr_in si_other;
	int s, i, slen=sizeof(si_other);
	char buf[BUFLEN];
	char message[BUFLEN];

	if ( (s=socket(AF_INET, SOCK_DGRAM, IPPROTO_UDP)) == -1)
	{
		printf("socket error");
		exit(1);
	}

	memset((char *) &si_other, 0, sizeof(si_other));
	si_other.sin_family = AF_INET;
	si_other.sin_port = htons(PORT);
	
	if (inet_aton(SERVER , &si_other.sin_addr) == 0) 
	{
		fprintf(stderr, "inet_aton() failed\n");
		exit(1);
	}






        bzero(&si_other.sin_zero, 8);
        fp = fopen("1.txt", "rb");
        if(fp != NULL)
        printf("send file");
        else {
        printf("open file failed\n");
        exit(-1);
    }



































	while(1)
	{
		//printf("Enter message : ");
		if((len = fread(readBuff, 1, MSGLEN, fp)) > 0) {
                /*if(send(s, readBuff, len, 0) < 0){
                    perror("send() error");
                    exit(-1);
                } */
                if (sendto(s, readBuff, strlen(readBuff) , 0 , (struct sockaddr *) &si_other, slen)==-1)
		{
			printf("sendto error");
			return 1;
		}
                else {
                    printf(".");
                    bzero(&readBuff, MSGLEN);    
                }                
            } 
             else if(len == 0){  //等于0表示文件已到末尾
    //            send(sockfd, readBuff, strlen(readBuff), 0);
                printf("\nfile send success\n");
                break;
            } 
            else {
                perror("read() error");
                exit(-1);
            }
        }
    

    fclose(fp);
    


	return 0;
}
