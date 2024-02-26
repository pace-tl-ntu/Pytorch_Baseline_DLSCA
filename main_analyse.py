import os

import numpy as np

total_num_models = 100
dataset = "./"
model_type = "cnn" #mlp, cnn
leakage = "HW" #ID, HW

for byte in range(0,16):
    root = "./Result/"
    save_root = root+dataset+"_"+model_type+ "_byte"+str(byte)+"_"+leakage+"/"
    model_root = save_root+"models/"
    # print("root:", root)
    print("save_time_path:", save_root)
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(save_root):
        os.mkdir(save_root)
    if not os.path.exists(model_root):
        os.mkdir(model_root)
    best_model = -1
    best_NTGE = 2000
    best_GE = 256
    for num_models in range(total_num_models):
        result = np.load(model_root + "/result_" +str(num_models ) +"_byte" +str(byte)+".npy", allow_pickle=True).item() #{"GE": GE, "NTGE": NTGE}
        NTGE = result["NTGE"]
        GE = result["GE"]
        if NTGE < best_NTGE:
            best_model = num_models
            best_NTGE = NTGE
        if GE[-1]< best_GE:
            best_GE = GE[-1]


    print("Byte: ", byte )
    print("best_model: ", best_model )
    print("best_NTGE: ", best_NTGE )
    print("best_GE: ", best_GE )
    print("-----"*10)