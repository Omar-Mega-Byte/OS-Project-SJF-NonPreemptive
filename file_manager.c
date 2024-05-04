#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char path[100], num[100], dest[100], command[200];

void listFiles() {
    strcpy(command, "ls ");
    printf("Please enter the path of the file that you want to list its files:\n");
    scanf("%s", path);
    strcat(command, path);
    system(command);
}

void create() {
    strcpy(command, "mkdir ");
    printf("Please enter the path of the file:\n");
    scanf("%s", path);
    system(strcat(command, path));
}

void delete() {
    strcpy(command, "rmdir ");
    printf("Please enter the path of the file:\n");
    scanf("%s", path);
    system(strcat(command, path));
}

void createSymbolicLink() {
    strcpy(command, "ln -s ");
    printf("Please enter the path of the file:\n");
    scanf("%s", path);

    printf("Enter the destination of the file:\n");
    scanf("%s", dest);

    strcat(command, path);
    strcat(command, " ");
    strcat(command, dest);

    system(command);
}

void changePermissions() {
    strcpy(command, "sudo chmod ");
    printf("Please enter the permissions for the file.\n");
    printf("Use the following format: [read/write/execute],[owner/group/other]\n");
    printf("Permissions (r/w/x),(O/G/N): ");
    scanf("%s", num);
    printf("Enter the path of the file:\n");
    scanf("%s", path);
    strcat(command, num);
    strcat(command, " ");
    strcat(command, path);
    system(command);
}



int main() {
    int choice;

    while (1) {
        printf("\nFile Manager\n");
        printf("1. List files/directories\n");
        printf("2. Change permissions of files\n");
        printf("3. Make files/directories\n");
        printf("4. Delete files/directories\n");
        printf("5. Create symbolic link files\n");
        printf("6. Exit\n");

        printf("Enter your choice: ");
        scanf("%d", &choice);

        switch(choice) {
            case 1:
                listFiles();
                break;
            case 2:
                changePermissions();
                break;
            case 3:
                create();
                break;
            case 4:
                delete();
                break;
            case 5:
                createSymbolicLink();
                break;
            case 6:
                printf("Exiting...\n");
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    }
}
