import torch
print(torch.__version__)
print(torch.cuda.is_available())

'''
如果遇到 cuda 不能使用的情况 可以参考以下这些方案

查看本地的cuda和pytorch的版本是否对应
参考以下网站
https://pytorch.org/get-started/previous-versions/

例如
# ROCM 5.6 (Linux only)
pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/rocm5.6
# CUDA 11.8
pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu118
# CUDA 12.1
pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cu121
# CPU only
pip install torch==2.2.0 torchvision==0.17.0 torchaudio==2.2.0 --index-url https://download.pytorch.org/whl/cpu
按照自己cuda的版本去运行对应的命令
'''