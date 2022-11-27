# train_config
test_time = False
data_offset = 'D:/wzc'
train = {}
train['train_DPDD_img_path']    = data_offset+'/dd_dp_dataset_png/train_c/source'
train['train_DPDD_gt_path']     = data_offset+'/dd_dp_dataset_png/train_c/target'
train['train_LFDOF_img_path']   = data_offset+'/LFDOF/train_data/input'
train['train_LFDOF_gt_path']    = data_offset+'/LFDOF/train_data/ground_truth'
train['test_DPDD_img_path']     = data_offset+'/dd_dp_dataset_png/test_c/source'
train['test_DPDD_gt_path']      = data_offset+'/dd_dp_dataset_png/test_c/target'
train['test_LFDOF_img_path']    = data_offset+'/LFDOF/test_data/input'
train['test_LFDOF_gt_path']     = data_offset+'/LFDOF/test_data/ground_truth'
train['test_RealDOF_img_path']  = data_offset+'/RealDOF/source'
train['test_RealDOF_gt_path']   = data_offset+'/RealDOF/target'
train['test_RTF_img_path']      = data_offset+'/RTFDataset/image/0'
train['test_RTF_gt_path']       = data_offset+'/RTFDataset/GT'
# train['test_img_path']=data_offset+'/RTFDataset/image/1.6'
# train['test_gt_path'] = data_offset+'/RTFDataset/GT'
train['batch_size'] = 4
train['val_batch_size'] = 4
train['test_batch_size'] = 1
train['num_epochs'] = 5000
train['num_fine_tune_epochs'] = 2000
train['log_epoch'] = 1
train['optimizer'] = 'Adam'
train['learning_rate'] = 1e-4

# -- for SGD -- #
train['momentum'] = 0.9
train['nesterov'] = True

# config for save , log and resume
train['sub_dir'] = 'checkpoints'
train['resume'] = './save/checkpoints/0'
train['resume_epoch'] = None  # None means the last epoch
train['resume_optimizer'] = './save/checkpoints/0'

net = {}
net['xavier_init_all'] = True

loss = {}
loss['weight_l2_reg'] = 0
