import json
import glob


data_dir = 'Data/'
valid = set(['water', 'island'])

def test_for_labels(valid_labels = valid):

    def get_input_files(data_dir = data_dir):
        jsonFiles = []
        filetypes = data_dir + '*.json'
        for file in glob.glob(filetypes):
            jsonFiles.append(file)
        return jsonFiles

    def get_attribute_for_hierarchy(data, key_order, index):
        if index >= len(key_order):
            return data
        sub_data = data[key_order[index]]
        index += 1
        return get_attribute_for_hierarchy(sub_data, key_order, index)

    def get_attributes_from_file(file):
        with open(jf) as ojf:
            d = json.load(ojf)
        return d

    jsonFiles = get_input_files()
    
    for jf in jsonFiles:
        d = get_attributes_from_file(jf)
        for key in d.keys():
            regions = get_attribute_for_hierarchy(d, [key, 'regions'], 0)
            num_regions = len(regions)
            print(f'{key} # regions = {num_regions}')
            for i in range(0, num_regions):
                index = str(i)
                region_attrib = regions[index]['region_attributes']
                assert region_attrib['label'] in valid_labels
    print("**Test completed**")

                
test_for_labels()


