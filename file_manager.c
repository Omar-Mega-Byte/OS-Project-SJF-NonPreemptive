#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void listFiles() {
    system("ls -l");
}

void changePermissions() {
    char filename[100];
    int permissions;

    printf("Enter file name: ");
    scanf("%s", filename);
    printf("Enter new permissions (e.g., 755): ");
    scanf("%d", &permissions);

    char command[200];
    sprintf(command, "chmod %d %s", permissions, filename);
    system(command);
}

void create() {
    char dirname[100];
    char filename[100];

    printf("Enter directory name to create: ");
    scanf("%s", dirname);
    char mkdirCommand[200];
    sprintf(mkdirCommand, "mkdir %s", dirname);
    system(mkdirCommand);

}
void delete() {
    char name[100];
    printf("Enter file/directory name to delete: ");
    scanf("%s", name);

    char command[200];
    sprintf(command, "rm -rf %s", name);
    system(command);
}

void createSymbolicLink() {
    char target[100];
    char linkname[100];

    printf("Enter target file/directory: ");
    scanf("%s", target);
    printf("Enter link name: ");
    scanf("%s", linkname);

    char symlinkCommand[300];
    strcpy(symlinkCommand, "ln -s ");
    strcat(symlinkCommand, target);
    strcat(symlinkCommand, " ");
    strcat(symlinkCommand, linkname);
    strcat(symlinkCommand, "-sym");
    system(symlinkCommand);
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
