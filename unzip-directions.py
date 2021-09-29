import zipfile
import shutil

dir_to_zip = '/Users/seanshea/PycharmProjects/udemy'
output_filename = 'unzip_me_for_instructions'
shutil.make_archive(output_filename, 'zip', dir_to_zip)
shutil.unpack_archive('unzip_me_for_instructions.zip', 'instructions_unzip', 'zip')