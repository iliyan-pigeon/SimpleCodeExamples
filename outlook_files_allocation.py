import os
import win32com.client
import datetime
import zipfile


def save_attachments(subject_filter, attachment_ext, save_folder):
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    inbox = outlook.GetDefaultFolder(6)  # 6 refers to the Inbox
    messages = inbox.Items
    messages.Sort("[ReceivedTime]", True)  # Sort by received time descending
    today = datetime.date.today()

    for message in messages:
        if message.Subject == subject_filter and message.ReceivedTime.date() == today:
            attachments = message.Attachments
            for attachment in attachments:
                if attachment.FileName.endswith(attachment_ext):
                    attachment_path = os.path.join(save_folder, attachment.FileName)
                    attachment.SaveAsFile(attachment_path)
                    print(f"Saved: {attachment.FileName}")

                    with zipfile.ZipFile(attachment_path, 'r') as zip_ref:
                        zip_ref.extractall(save_folder)
                        print(f"Extracted: {attachment.FileName} to {save_folder}")

                    os.remove(attachment_path)
                    print(f"Deleted {attachment_path}")


def loop_the_emails():
    # Date format for the project name
    date = str(datetime.date.today()).split("-")
    date = f"{date[2]}.{date[1]}.{date[0]}"

    processes_information = [[f"subject_one", ".zip", "location_one"],
                           [f"subject_two", ".zip", "location_two"],
                           [f"subject_three", ".zip", "location_three"],
                           [f"subject_four", ".zip", "location_four"]]

    for process in processes_information:
        email_subject = process[0]
        file_extension = process[1]
        directory = process[2]

        save_attachments(email_subject, file_extension, directory)
        print("File saved")

    print("All files are saved")


if __name__ == "__main__":
    loop_the_emails()
