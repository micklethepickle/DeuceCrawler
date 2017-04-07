#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(void){
	char *token;
	char S[8]="+=, ;&%";

	char *data = getenv("QUERY_STRING");
	//char data[100]="commands=EXIT inventory 10 10";
	token = strtok(data, S);
	printf("Content-type:text/html\n\n");
	printf("<!DOCTYPE html>"
		"<html>");
	/* walk through other tokens */
   	while( token != NULL ) 
   	{
      		printf( "<p>%s</p>", token );
    
     	 	token = strtok(NULL, S);
   	}

	printf("</html>");
}
