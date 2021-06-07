import xml.etree.ElementTree as ET
import os
import shutil


def run_cfg(cfg_name='cfg1.xml'):
    parser = ET.XMLParser(encoding='utf-8')
    tree = ET.parse(cfg_name, parser)
    root = tree.getroot()
    files = root.findall('file')
    for file in files:
        srcf = file.get('source_path')
        dstf = file.get('destination_path')
        name = file.get('file_name')
        if os.path.exists(os.path.join(srcf, name)):
            if os.path.exists(dstf):
                shutil.copyfile(os.path.join(srcf, name), os.path.join(dstf, name))
                print(f'File {name} copied successfully.')
            else:
                print('Invalid destination path.')
        else:
            print('Invalid source path.')
    return


if __name__ == '__main__':
    read_cfg()
