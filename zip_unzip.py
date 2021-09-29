import zipfile
import shutil

f = open('fileone.txt', 'w+')
f.write('One File')
f.close()

f = open('filetwo.txt', 'w+')
f.write("Two File")
f.close()

compfile = zipfile.ZipFile('comp_file.zip', 'w')
compfile.write('fileone.txt', compress_type=zipfile.ZIP_DEFLATED)
compfile.write('filetwo.txt', compress_type=zipfile.ZIP_DEFLATED)
compfile.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')

dir_to_zip = '/Users/seanshea/PycharmProjects/udemy/extracted_content'
output_filename = 'example'
shutil.make_archive(output_filename, 'zip', dir_to_zip)
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')