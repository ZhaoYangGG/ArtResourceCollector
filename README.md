# ArtResourceCollector

ArtResourceCollector is a tool for collecting image names from a folder and retrieving related summaries from Wikipedia, then saving this information into an Excel file.

## Dependencies

Make sure you have the following dependencies installed:

- `openpyxl`
- `wikipedia-api`

You can install these dependencies using the following command:

```sh
pip install -r 
requirements.txt
```

## Usage

1. Update the `image_folder` variable in the `excle.py` file with the path to your image folder.
2. Run the `excle.py` script:

```sh
python 
excle.py
```

3. The script will iterate through all image files in the folder, get the file names, retrieve related summaries from Wikipedia, and save this information into the `art_resources_0.xlsx` file.

## File Structure

```
.DS_Store
excle.py
requirements.txt
```
- `excle.py`: Main script file.
- `requirements.txt`: Dependencies file.

## Notes

- Make sure the path to your image folder is correct.
- Ensure you have a stable internet connection to access the Wikipedia API.

## License

This project is licensed under the MIT License. For more information, see the LICENSE file.