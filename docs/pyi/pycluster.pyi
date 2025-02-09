from __future__ import annotations
import typing
__all__ = ['BODY', 'FACE', 'INT_MAX', 'c_threadid', 'cluster_div_mem_error', 'cluster_hdl', 'cluster_invoke_error', 'cluster_license_error', 'cluster_logic_error', 'default_cfg', 'demo_version', 'detail_info', 'detail_info_viewer', 'doc', 'lib_version', 'mdl_e', 'platform', 'sdk_version', 'this_platform']
class cluster_div_mem_error(Exception):
    pass
class cluster_hdl:
    @typing.overload
    def __init__(self, arg0: list[mdl_e], arg1: dict[str, str]) -> None:
        """
                根据配置字典构造算法句柄，其字典类型为dict[str, str]， 即键值均为字符串的字典，如：
                例如：
                ``` python
        
                def to_str_dict(func):
                    def wrapper() -> 'dict[str, str]':
                        res : dict = func()
                        return dict(map(lambda item: (item[0], str(item[1])), res.items()))
                    return wrapper
        
                @to_str_dict
                def cfg() -> dict:
                    return {
                        "face_cfg_file" : "../model/face/fcl_v1.6",         # 人脸模型路径
                        "body_cfg_file" : "../model/body/body.json",        # 人体模型路径
                        "device_id" : 1,                                    # 设备id
                        "device_type" : 2,                                  # 设备类型，2为gpu，1为cpu
                        "save" : False,                                     # 是否保存离线合档中间结果
                        "record" : True,                                    # 是否保存数据探针结果
                        "body_centroid_num" : 4,                            # 人体质心数
                        "face_feat_dim" : 256,                              # 人脸特征维度
                        "body_feat_dim" : 256,                              # 人体特征维度
                        "face_one_max_result_num" : 10,                     # 人脸oc最大结果数
                        "body_one_max_result_num" : 10,                     # 人体oc最大结果数
                        "feature" : "fp16",                                 # 人脸特征类型，fp32不填即可
                        "proxy_sub_lower_bound" : 8                         # 实时底档筛选规则的底档数量
                    }
        
                alg_hdl = pycluster.cluster_hdl([pycluster.FACE, pycluster.BODY], cfg())
                ```
                上述例子中cfg()构造了一个字典，并使用修饰器将值转化为字符串，并传给pycluster.cluster_hdl构造函数创建了一个算法句柄alg_hdl
                这里cfg也可以使用默认参数 pycluster.default_cfg()
        """
    @typing.overload
    def __init__(self, arg0: list[mdl_e], arg1: str) -> None:
        ...
    def get_cfg(self) -> dict[str, str]:
        ...
class cluster_invoke_error(Exception):
    pass
class cluster_license_error(Exception):
    pass
class cluster_logic_error(Exception):
    pass
class detail_info_viewer:
    """
    信息
    """
    def __enter__(self) -> detail_info_viewer:
        ...
    def __exit__(self, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> None:
        ...
    def __getitem__(self, arg0: str) -> typing.Any:
        ...
    def __repr__(self) -> str:
        ...
    def as_dict(self) -> dict:
        ...
    def clear(self) -> None:
        ...
    def local(self) -> detail_info_viewer:
        ...
class mdl_e:
    """
    
            聚类模态枚举，其中：
            FACE 即 DHIVS_CLUSTER_FACE
            BODY 即 DHIVS_CLUSTER_BODY
        
    
    Members:
    
      FACE : FACE 即人脸模态 DHIVS_CLUSTER_FACE
    
      BODY : BODY 即人体模态 DHIVS_CLUSTER_BODY
    """
    BODY: typing.ClassVar[mdl_e]  # value = <mdl_e.BODY: 2>
    FACE: typing.ClassVar[mdl_e]  # value = <mdl_e.FACE: 1>
    __members__: typing.ClassVar[dict[str, mdl_e]]  # value = {'FACE': <mdl_e.FACE: 1>, 'BODY': <mdl_e.BODY: 2>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class platform:
    """
    
            平台枚举
        
    
    Members:
    
      UNKONWN
    
      X86_CPU
    
      X86_GPU
    
      ARM
    
      ASCEND710
    
      CAMBRICON220
    
      AX650
    """
    ARM: typing.ClassVar[platform]  # value = <platform.ARM: 45>
    ASCEND710: typing.ClassVar[platform]  # value = <platform.ASCEND710: 30>
    AX650: typing.ClassVar[platform]  # value = <platform.AX650: 71>
    CAMBRICON220: typing.ClassVar[platform]  # value = <platform.CAMBRICON220: 35>
    UNKONWN: typing.ClassVar[platform]  # value = <platform.UNKONWN: 0>
    X86_CPU: typing.ClassVar[platform]  # value = <platform.X86_CPU: 1>
    X86_GPU: typing.ClassVar[platform]  # value = <platform.X86_GPU: 65537>
    __members__: typing.ClassVar[dict[str, platform]]  # value = {'UNKONWN': <platform.UNKONWN: 0>, 'X86_CPU': <platform.X86_CPU: 1>, 'X86_GPU': <platform.X86_GPU: 65537>, 'ARM': <platform.ARM: 45>, 'ASCEND710': <platform.ASCEND710: 30>, 'CAMBRICON220': <platform.CAMBRICON220: 35>, 'AX650': <platform.AX650: 71>}
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
def c_threadid() -> int:
    """
            默认配置表
            例如：
            ``` python
    
            from pycluster2x import pycluster, pydossier, pypic, pycache
            print(pycluster.c_threadid())
            ```
    """
def default_cfg() -> dict[str, str]:
    """
            默认配置表
            例如：
            ``` python
    
            from pycluster2x import pycluster, pydossier, pypic, pycache
            print(pycluster.default_cfg())
            ```
    """
def demo_version() -> tuple[int, str, str]:
    """
            获取聚类demo库版本号
            例如：
            ``` python
    
            import json
            from pycluster2x import pycluster
            with open("svn.log", "w+") as f:
                svn = {"demo_version":pycluster.demo_version()}
                json.dump(svn, f)
            ```
            上述代码获得了demo版本，并写在了json中
    """
def detail_info() -> detail_info_viewer:
    ...
def doc() -> None:
    ...
def lib_version() -> tuple[int, str, str]:
    """
            获取聚类so库版本号
            例如：
            ``` python
    
            import json
            from pycluster2x import pycluster
            with open("svn.log", "w+") as f:
                svn = {"lib_version":pycluster.lib_version()}
                json.dump(svn, f)
            ```
            上述代码获得了库版本，并写在了json中
    """
def sdk_version() -> tuple[int, str, str]:
    """
            获取聚类so库版本号
            例如：
            ``` python
    
            import json
            from pycluster2x import pycluster
            with open("svn.log", "w+") as f:
                svn = {"sdk_version":pycluster.sdk_version()}
                json.dump(svn, f)
            ```
            上述代码获得了集成版本，并写在了json中
    """
def this_platform() -> platform:
    """
            获取平台类型
    """
BODY: mdl_e  # value = <mdl_e.BODY: 2>
FACE: mdl_e  # value = <mdl_e.FACE: 1>
INT_MAX: int = 2147483647
