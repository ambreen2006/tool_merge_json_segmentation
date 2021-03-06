# tool_merge_json_segmentation

## Files

1. **Merge_multiple_json_files.ipynb** Code that reads json files from the data folder specified and 
writes a merged json to the `Annotations` directory.

2. **Data** Directory containing the input json files

3. **Annotations** Output files

4. **verify_data.py** Python script to verify that the region labels are either 'water' or 'island'. 

## Workflow

1. Place all the input json files in the 'Data' directory. This reference to the input directory 
can be changed. Please refer to the Notebook for changing the name.

2. Customize the name for the merged output file if needed.

3. Run all the cells

## Output / Result

1. A merged **json** file with the current timestamp would be written to the output directory.

E.g output json filename: `merged_2020_05_26.json`

2. A **txt** file with all the name of the input json file would be written to the output directory

E.g. output txt filename: `original_filenames_2020_05_26_merged.txt`

Note: Output directory can also be customized, please refer to the notebook