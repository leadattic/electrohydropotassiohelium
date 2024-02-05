#include <stdio.h>
#include <stdlib.h>



void std_exit(int code){
    exit(code);
}
void std_print(char str[]){

    for(int i = 0; i < no_access_arr_length(str); i++){
        printf("%c", str[i]);
    }
    
    }

int no_access_arr_length(char arr[])
{
    int i;
    int count = 0;
    for(i=0; arr[i]!='\0'; i++)
    {
        count++;
    }
    return count;
}

int no_access_arr_length(int arr[])
{
    int i;
    int count = 0;
    for(i=0; arr[i]!='\0'; i++)
    {
        count++;
    }
    return count;
}