import os
os.system("cd NeWCRFs-master/NeWCRFs-master & python newcrfs/test.py --data_path datasets/test_data --dataset nyu --filenames_file data_splits/test_list.txt --checkpoint_path model_nyu.ckpt --max_depth 10 --save_viz")
os.system("python persondetect/test.py")