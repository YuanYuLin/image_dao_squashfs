import ops
import iopc

pkg_path = ""
output_dir = ""
output_rootfs_dir = ""
squashfs_name = "dao.squashfs"

def set_global(args):
    global pkg_path
    global output_dir 
    global output_rootfs_dir
    global output_platform_dir
    global daosfs_script
    pkg_path = args["pkg_path"]
    output_dir = args["output_path"]
    output_platform_dir = ops.path_join(iopc.getOutputRootDir(), "platform")
    daosfs_script = ops.path_join(output_platform_dir, "daosfs.py")
    #output_rootfs_dir = ops.getEnv("LINUXKERNELMODULEROOT")

def MAIN_ENV(args):
    set_global(args)
    return False

def MAIN_EXTRACT(args):
    set_global(args)
    return True

def MAIN_PATCH(args, patch_group_name):
    set_global(args)
    for patch in iopc.get_patch_list(pkg_path, patch_group_name):
        if iopc.apply_patch(output_dir, patch):
            continue
        else:
            sys.exit(1)

    return True

def MAIN_CONFIGURE(args):
    set_global(args)

    return False

def MAIN_BUILD(args):
    set_global(args)

    #iopc.make_squashfs_xz(output_platform_dir, output_dir, squashfs_name)
    CMD=['python', daosfs_script, output_platform_dir, ops.path_join(output_dir, squashfs_name)]
    ops.execCmd(CMD, output_dir, False)

    return False

def MAIN_INSTALL(args):
    set_global(args)

    ops.sudo_copyto(ops.path_join(output_dir, squashfs_name), iopc.getOutputRootDir())
    return False

def MAIN_SDKENV(args):
    set_global(args)

    return False

def MAIN_CLEAN_BUILD(args):
    set_global(args)

    return False

def MAIN(args):
    set_global(args)
    print "image squashfs"

