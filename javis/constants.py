import os

data_folder = 'data'

javis_output_file = os.path.join(data_folder, 'output.log')
javis_config_file = os.path.join(data_folder, 'config.ini')
section_listener = 'listener'
config_listener_pos = section_listener, 'pos'
