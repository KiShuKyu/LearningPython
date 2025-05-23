
from pymongo import MongoClient
from bson import ObjectId


client = MongoClient(
    "mongodb+srv://zoloronoloa:pass@lesson.idrdxzg.mongodb.net/", tlsAllowInvalidCertificates=True)

print(client)
db = client["ytmanager"]
video_collection = db["videos"]


def list_videos():
    for video in video_collection.find({}):
        print(
            f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")


def add_videos(name, time):
    video_collection.insert_one({"name": name, "time": time})


def update_videos(video_id, new_name, new_time):
    video_collection.update_one(
        {'_id': ObjectId(video_id)},
        {"$set": {"name": new_name, "time": new_time}}
    )


def delete_videos(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})


def main():
    while True:
        print("\n Youtube Manager App.")
        print("1. List all video.")
        print("2. Add a new video.")
        print("3. Update a video.")
        print("4. Delete the video.")
        print("5. Exit the app.")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the video name: ")
            time = input("Enter the video time: ")
            add_videos(name, time)
        elif choice == '3':
            video_id = input("Enter the video id to update: ")
            name = input("Enter the updates video name: ")
            time = input("Enter the updated video time: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = input("Enter the video id to delete: ")
            delete_videos(video_id)
        elif choice == '5':
            break
        else:
            print("You must Enter a valid number.")


if __name__ == "__main__":
    main()
