import os
import numpy as np
from glob import glob

def load_flist(flist, substr='', ext=['.jpg', '.png'], recursive=False):
    if isinstance(flist, list):
        return flist

    if isinstance(flist, np.ndarray):
        return flist

    # flist: image file path, image directory path, text file flist path
    if isinstance(flist, str):
        if os.path.isdir(flist):
            if not recursive:
                _flist = flist
                flist = []
                for _ext in ext:
                    flist += [os.path.abspath(fn) for fn in glob(_flist + '/*%s' %(_ext)) if substr in os.path.basename(fn)]
            else:
                walk = os.walk(flist)
                flist = []
                for parentname, _, filelist in walk:
                    flist += [os.path.abspath(os.path.join(parentname, fn)) for fn in filelist if os.path.splitext(fn)[-1].lower() in ext and substr in fn]

            flist.sort()
            return flist

        if os.path.isfile(flist):
            try:
                flist = np.genfromtxt(flist, dtype=np.str, encoding='utf-8')
                if flist.ndim > 1 :
                    flist = flist[:, 0]
                return flist.tolist()
            except:
                return [flist]

    return []


if __name__ == "__main__":
    size = 256

    image_root = "images"
    mask_root = "masks"
    output_root = "output"
    time_log = "test_time.log"

    # flist = np.genfromtxt("./image_files/inpainting/places2_testlist_large", dtype=np.str, encoding="utf-8")
    # image_flist = [os.path.join(image_root, os.path.basename(fn)) for fn in flist[:,0]]
    # mask_flist = [os.path.join(mask_root, "mask_"+os.path.basename(fn)) for fn in flist[:,1]]

    image_flist = load_flist(image_root)
    mask_flist = load_flist(mask_root)

    # import ipdb; ipdb.set_trace()

    for i in range(len(image_flist)):
        print("\rprogress: %d/%d"%(i, len(image_flist)), end="")
        image_path = image_flist[i]
        mask_path = mask_flist[i]
        basename = os.path.basename(image_path)[:-4]
        output_path = os.path.join(output_root, "%s.png"%basename)
        log_path = "./metrics.log"
        cmd = "../../build/patchmatch %s %s %s %s %05d >> %s"%(image_path, mask_path, output_path, log_path, i, time_log)
        #print(cmd)

        # import ipdb; ipdb.set_trace()
        os.system(cmd)