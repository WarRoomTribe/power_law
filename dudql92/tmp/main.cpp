#include <stdio.h>
#include <io.h>
#include <conio.h>
#include <string.h>
#include <corecrt_io.h>

void search(char* buf, int cnt)
{
	_finddata_t fd;
	long handle;
	int result = 1;
	char tmp[1024];
	memcpy(tmp, buf, 1024);
	int i;

	strcat(tmp,"\\*");
	handle = _findfirst(tmp, &fd);  //현재 폴더 내 모든 파일을 찾는다.

	if (handle == -1)
	{
		printf("There were no files.\n");
		return;
	}

	while (result != -1)
	{
		if (fd.attrib == 0x10) {
			if (!strcmp(fd.name, ".")) {
				for (i = 0; i < cnt; i++) {
					printf("\t");
				}
				printf("Dir: %s\n", fd.name);
				result = _findnext(handle, &fd);
				continue;
			}
			if (!strcmp(fd.name, "..")) {
				for (i = 0; i < cnt; i++) {
					printf("\t");
				}
				printf("Dir: %s\n", fd.name);
				result = _findnext(handle, &fd);
				continue;
			}
			for (i = 0; i < cnt; i++) {
				printf("\t");
			}
			printf("Dir: %s\n", fd.name);
			
			memcpy(tmp, buf, 1024);
			strcat(tmp, "\\");
			strcat(tmp, fd.name);
			search(tmp,cnt+1);
		}
		else {
			printf("File: %s\n", fd.name);
		}
		result = _findnext(handle, &fd);
	}

	_findclose(handle);

}

int main(void) {
	char buf[1024] = "C:\\";//Users\\Administrator\\Desktop\\foresnsic";
	search(buf,0);
	return 0;
}