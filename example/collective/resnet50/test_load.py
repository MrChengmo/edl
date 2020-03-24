import paddle.fluid as fluid
import numpy as np
def load_to_np(emb_path):
    program = fluid.Program()
    block = program.global_block()

    emb = block.create_var(name="EMB",
                     persistable=True,
                     type=fluid.core.VarDesc.VarType.LOD_TENSOR,
                     dtype="int64",
                     shape=[1],
                     lod_level=0)

    block.append_op(
                    type='load',
                    inputs={},
                    outputs={'Out': [emb]},
                    attrs={'file_path': emb_path})
    exe=fluid.Executor(fluid.CPUPlace())
    exe.run(program)
    return np.array(fluid.global_scope().find_var(emb.name).get_tensor())

print(load_to_np("/root/go/src/github.com/PaddlePaddle/Fleet/benchmark/collective/resnet/fleet_checkpoints/__paddle_fleet_checkpoint__.0/@LR_DECAY_COUNTER@"))