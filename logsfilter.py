import os
import os.path
import pandas as pd

def logsfilter():

    dir = "C:\\Users\\USER\\Desktop\\Python\\Scripts\\logs"

    file_result = "C:\\Users\\USER\\Desktop\\Python\\Scripts\\Destiny\\result.txt"

    same_words = ["Move files", "Connected to the SFTP", "Files moved successfully", "Down" , "0x00",  "Starting the script"]


    try:
        dir_files = os.listdir(dir)
    except FileNotFoundError:
        print(f"Directory '{dir}' not found!")
        return

    print("Files in directory:", dir_files)

    with open(file_result, "w") as result_file:
        
        for file in dir_files:
            # Construct the full path to the file
            file_path = os.path.join(dir, file)

            print(f"Processing file: {file_path}")

            try:
                
                df = pd.read_csv(file_path)

                selected_columns = df[["ACTION", "STATUS", "SUMMARY"]]

                # Combine selected columns into a single string for each row
                combined = selected_columns.apply(lambda row: " ".join(row.values.astype(str)), axis=1)

                # Remove words/phrases in same_words
                for word in same_words:
                    combined = combined.str.replace(word, "", regex=False)

                # Filter out empty rows after removing words/phrases
                filtered = combined[combined.str.strip() != ""]

                # Write the filtered content to the result file
                if not filtered.empty:
                    result_file.write(f"Content from {file}:\n")
                    result_file.write("\n".join(filtered))
                    result_file.write("\n\n")  # Add spacing between file contents

                    print(f"Processed content from {file}")
            except Exception as e:
                    print(f"Error processing file '{file_path}': {e}")
logsfilter()



