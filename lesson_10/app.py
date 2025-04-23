import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w')as file:
        json.dump(videos, file)


def list_all_vds(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*" * 70)


def add_vds(videos):
    name = input("Enter the name of the video:")
    time = input("Enter video time:")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_vds(videos):
    list_all_vds(videos)
    index = int(input("Enter the video number to update"))
    if 1 <= index <= len(videos):
        name = input("Enter the new video name:")
        time = input("Enter the new video time:")
        videos[index-1] = {'name': name, 'time': time}
        save_data_helper(videos)
    else:
        print("Invalid index selected.")


def del_vds(videos):
    list_all_vds(videos)
    index = int(input("Enter the video number you would like to delete:\n"))
    if 1 <= index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected.")


def main():

    videos = load_data()

    while True:
        print("\n Youtube Manager")
        print("\n What would you like to do.")
        print("1. List a favourite videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choice = input("Enter your choice:\n")
        # print(videos)

        match choice:
            case '1':
                list_all_vds(videos)
            case '2':
                add_vds(videos)
            case '3':
                update_vds(videos)
            case '4':
                del_vds(videos)
            case '5':
                break
            case _:
                print("Invalid Choice")


if __name__ == "__main__":
    main()
