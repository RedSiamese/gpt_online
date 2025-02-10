from __future__ import annotations
import numpy
import pycluster2x.lib.pycluster
import typing
__all__ = ['async_pb_input_csv', 'async_unser', 'doc', 'pb_input_csv', 'pic_info', 'sp_info', 'unser']
class pic_info:
    """
    抓拍集类, 即cluster_pb_input类，其中保存了抓拍的特征、属性和关联关系
    """
    class pic_feature_viewer_t:
        """
        特征
        """
        def __enter__(self) -> dict[pycluster2x.lib.pycluster.mdl_e, numpy.ndarray[numpy.float32]]:
            ...
        def __exit__(self, arg0: typing.Any, arg1: typing.Any, arg2: typing.Any) -> None:
            ...
    def __add__(self, arg0: pic_info) -> pic_info:
        """
                将两个档案集进行叠加，不去重，于 += 相同
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
                it:pycache.db_it = db.get_time_it(0)               # 根据时间流，从时间流最开始，获取时间流最初的数据迭代器
                pb_info_1:pypic.pic_info = it.get(10)                       # 从迭代器获取10张抓拍，组成抓拍集，迭代器往后移动10张
                pb_info_2:pypic.pic_info = it.get(10)                       # 从迭代器获取10张抓拍，组成抓拍集，迭代器往后移动10张
        
                print(pb_info_1, pb_info_2)
                pb = pb_info_1 + pb_info_2                                  # 将pb_info_1和pb_info_2加起来
                print(pb)
                ```
                如果存在重复的数据条目不会去重
        """
    @typing.overload
    def __getitem__(self, arg0: pycluster2x.lib.pycluster.mdl_e) -> pic_info:
        """
                获取某个模态独立的抓拍集
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb = db.get_partition("0-0")
                pb_face = pb[pycluster.FACE]
        
                print(pb, pb_face)
                ```
                上述代码取出了"0-0"分区中的人脸模态数据，变成了纯人脸数据
        """
    @typing.overload
    def __getitem__(self, arg0: int) -> pic_info:
        """
                获取第抓拍id(person_id)张抓拍
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb = db.get_partition("0-0")
                pb0 = pb[0]
        
                print(pb, pb0)
                ```
                上述代码取出了抓拍集抓拍id(pid)为0的抓拍
        """
    @typing.overload
    def __getitem__(self, arg0: str) -> pic_info:
        """
                获取第抓拍id(person_id)张抓拍
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb = db.get_partition("0-0")
                pb0 = pb["101129900132000373210220211230075200012120607705"]
        
                print(pb, pb0)
                ```
                上述代码取出了抓拍集抓拍id(pid)为0的抓拍
        """
    @typing.overload
    def __getitem__(self, arg0: slice) -> pic_info:
        """
                按切片获取第抓拍id(person_id)张抓拍
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb = db.get_partition("0-0")
                pb0 = pb[0:10]
        
                print(pb, pb0)
                ```
                上述代码取出了抓拍集抓拍id(pid)为0的抓拍
        """
    def __getstate__(self) -> list[int]:
        ...
    def __iadd__(self, arg0: pic_info) -> pic_info:
        """
                将两个档案集进行叠加，不去重，于 += 相同
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
                it:pycache.db_it = db.get_time_it(0)               # 根据时间流，从时间流最开始，获取时间流最初的数据迭代器
                pb_info_1:pypic.pic_info = it.get(10)                       # 从迭代器获取10张抓拍，组成抓拍集，迭代器往后移动10张
                pb_info_2:pypic.pic_info = it.get(10)                       # 从迭代器获取10张抓拍，组成抓拍集，迭代器往后移动10张
        
                print(pb_info_1, pb_info_2)
                pb_info_1 += pb_info_2                                      # 将pb_info_2加到pb_info_1中
                print(pb_info_1)
                ```
                如果存在重复的数据条目不会去重
        """
    @typing.overload
    def __init__(self) -> None:
        """
                构造一个空抓拍集类：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                pb = pypic.pic_info()
                ```
        """
    @typing.overload
    def __init__(self, info_list: list) -> None:
        """
                直接从一个数据序列（如python读的csv）获得抓拍集信息：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                data = [{'f_featuredata':numpy.array([0.1, -0.021, 0.121 ...]), 'f_qescore':0.92, 'f_clarity':0.75, 'p_featuredata':numpy.array([0.1, -0.021, 0.121 ...]), ...},
                        {'f_featuredata':numpy.array([0.1, -0.021, 0.121 ...]), 'f_qescore':0.53, 'f_clarity':0.86, 'p_featuredata':numpy.array([0.1, -0.021, 0.121 ...]), ...},
                        {'f_featuredata':numpy.array([0.1, -0.021, 0.121 ...]), 'f_qescore':0.12, 'f_clarity':0.73, 'p_featuredata':numpy.array([0.1, -0.021, 0.121 ...]), ...},
                        {'f_featuredata':numpy.array([0.1, -0.021, 0.121 ...]), 'f_qescore':0.42, 'f_clarity':0.45, 'p_featuredata':numpy.array([0.1, -0.021, 0.121 ...]), ...}] # 一系列数据
                pb = pypic.pic_info(data)
                ```
                其中，每一行为一条关联的抓拍(人脸人体)
                可包含结构化字段，有效字段为：
                    string                f_recordid
                    string                f_channelid
                    sint64                f_captime
                    string                f_imgurl
                    sint32                f_faceleft
                    sint32                f_facetop
                    sint32                f_faceright
                    sint32                f_facebottom
                    uint32                f_age
                    uint32                f_gender
                    uint32                f_race
                    uint32                f_ethniccode
                    uint32                f_eye
                    uint32                f_mouth
                    uint32                f_beard
                    uint32                f_mask
                    uint32                f_glasses
                    uint32                f_emotion
                    uint32                f_hat
                    uint32                f_pitch
                    uint32                f_yaw
                    uint32                f_roll
                    float                 f_clarity
                    uint32                f_qescore
                    float                 f_alignscore
                    float                 f_confidence
                    float                 f_completeness
                    uint32                f_illumination
                    uint32                f_saturation
                    string                f_extrecordid
                    string                f_algorithmversion
                    numpy.array           f_featuredata
                    double                f_gps_x
                    double                f_gps_y
                    sint32                f_track_id
        
        
                    string                p_recordid
                    string                p_channelid
                    sint64                p_captime
                    string                p_imgurl
                    sint32                p_bodyleft
                    sint32                p_bodytop
                    sint32                p_bodyright
                    sint32                p_bodybottom
                    float                 p_qe_score
                    uint32                p_hashead
                    uint32                p_hasheadreliability
                    uint32                p_hasvehicle
                    uint32                p_vehicletype
                    uint32                p_vehicletypereliability
                    uint32                p_hasdownbody
                    uint32                p_hasdownbodyreliability
                    uint32                p_posture
                    uint32                p_posturereliability
                    uint32                p_haserrordetect
                    uint32                p_uniformstyle
                    uint32                p_uniformstylereliability
                    uint32                p_hasraincoat
                    uint32                p_hasraincoatreliability
                    uint32                p_agebracket
                    uint32                p_agebracketreliability
                    uint32                p_gender
                    uint32                p_genderreliability
                    uint32                p_hatstyle
                    uint32                p_hatstylereliability
                    uint32                p_bagtype
                    uint32                p_bagtypereliability
                    uint32                p_upperbodyclothes
                    uint32                p_upperbodyclothesreliability
                    uint32                p_upperbodyclothestype
                    uint32                p_upperbodyclothestypereliability
                    uint32                p_upperbodycolor
                    uint32                p_upperbodycolorreliability
                    uint32                p_upperbodyvein
                    uint32                p_upperbodyveinreliability
                    uint32                p_hairstyle
                    uint32                p_hairstylereliability
                    uint32                p_haircolor
                    uint32                p_haircolorreliability
                    uint32                p_downperbodyclothes
                    uint32                p_downperbodyclothesreliability
                    uint32                p_downperbodycolor
                    uint32                p_downperbodycolorreliability
                    uint32                p_downperbodyvein
                    uint32                p_downperbodyveinreliability
                    string                p_algorithmversion
                    numpy.array           p_featuredata
                    double                p_gps_x
                    double                p_gps_y
                    sint32                p_track_id
                    float                 p_iqascore
                    uint32                p_haspicinfrared
                    uint32                p_nonmotorumbrellatype
                    uint32                p_nonmotorumbrellatypereliability
                    uint32                p_body_num
                    uint32                p_is_related_face
                    uint32                p_head_score
                    uint32                p_upbody_score
                    uint32                p_downbody_score
        """
    def __repr__(self) -> str:
        ...
    def __setstate__(self, arg0: list[int]) -> None:
        ...
    def add(self, other: pic_info) -> pic_info:
        """
                将两个档案集进行叠加，不去重，于 += 相同
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
                it:pycache.db_it = db.get_time_it(0)               # 根据时间流，从时间流最开始，获取时间流最初的数据迭代器
                pb_info_1:pypic.pic_info = it.get(10)                       # 从迭代器获取10张抓拍，组成抓拍集，迭代器往后移动10张
                pb_info_2:pypic.pic_info = it.get(10)                       # 从迭代器获取10张抓拍，组成抓拍集，迭代器往后移动10张
        
                print(pb_info_1, pb_info_2)
                pb_info_1.add(pb_info_2)                                    # 将pb_info_2加到pb_info_1中
                print(pb_info_1)
                ```
                如果存在重复的数据条目不会去重
                support asynchronous
        """
    def async_add(self, other: pic_info) -> pic_info:
        """
        
        async function of
        add(self: pycluster2x.lib.pypic.pic_info, other: pycluster2x.lib.pypic.pic_info) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_copy(self) -> pic_info:
        """
        
        async function of
        copy(self: pycluster2x.lib.pypic.pic_info) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_dump(self) -> list:
        """
        
        async function of
        dump(self: pycluster2x.lib.pypic.pic_info) -> list
            
        """
    def async_exclude(self, arg0: list[str]) -> pic_info:
        """
        
        async function of
        exclude(self: pycluster2x.lib.pypic.pic_info, arg0: list[str]) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_feature_set_enhancement(self, low: float = -0.5, high: float = 0.5) -> None:
        """
        
        async function of
        feature_set_enhancement(self: pycluster2x.lib.pypic.pic_info, low: float = -0.5, high: float = 0.5) -> None
            
        """
    def async_filter_from_level(self, lower: int, upper: int) -> pic_info:
        """
        
        async function of
        filter_from_level(self: pycluster2x.lib.pypic.pic_info, lower: int, upper: int) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_get_level(self, *args, **kwargs):
        """
        
        async function of
        get_level(self: pycluster2x.lib.pypic.pic_info, alg: pycluster2x.lib.pycluster.cluster_hdl) -> None
        get_level(self: pycluster2x.lib.pypic.pic_info, lower: int, upper: int) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_include(self, arg0: list[str]) -> pic_info:
        """
        
        async function of
        include(self: pycluster2x.lib.pypic.pic_info, arg0: list[str]) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_ser(self) -> bytes:
        """
        
        async function of
        ser(self: pycluster2x.lib.pypic.pic_info) -> bytes
            
        """
    def async_split(self, *args, **kwargs):
        """
        
        async function of
        split(self: pycluster2x.lib.pypic.pic_info) -> list[pycluster2x.lib.pypic.pic_info]
        split(self: pycluster2x.lib.pypic.pic_info, mode: str) -> list[pycluster2x.lib.pypic.pic_info]
        split(self: pycluster2x.lib.pypic.pic_info, num: int) -> list[pycluster2x.lib.pypic.pic_info]
            
        """
    def copy(self) -> pic_info:
        """
                把抓拍集复制一份
                support asynchronous
        """
    def dump(self) -> list:
        """
                可能包含的结构化有效字段为：
                    string                f_recordid
                    string                f_channelid
                    sint64                f_captime
                    string                f_imgurl
                    sint32                f_faceleft
                    sint32                f_facetop
                    sint32                f_faceright
                    sint32                f_facebottom
                    uint32                f_age
                    uint32                f_gender
                    uint32                f_race
                    uint32                f_ethniccode
                    uint32                f_eye
                    uint32                f_mouth
                    uint32                f_beard
                    uint32                f_mask
                    uint32                f_glasses
                    uint32                f_emotion
                    uint32                f_hat
                    uint32                f_pitch
                    uint32                f_yaw
                    uint32                f_roll
                    float                 f_clarity
                    uint32                f_qescore
                    float                 f_alignscore
                    float                 f_confidence
                    float                 f_completeness
                    uint32                f_illumination
                    uint32                f_saturation
                    string                f_extrecordid
                    string                f_algorithmversion
                    numpy.array           f_featuredata
                    double                f_gps_x
                    double                f_gps_y
                    sint32                f_track_id
        
        
                    string                p_recordid
                    string                p_channelid
                    sint64                p_captime
                    string                p_imgurl
                    sint32                p_bodyleft
                    sint32                p_bodytop
                    sint32                p_bodyright
                    sint32                p_bodybottom
                    float                 p_qe_score
                    uint32                p_hashead
                    uint32                p_hasheadreliability
                    uint32                p_hasvehicle
                    uint32                p_vehicletype
                    uint32                p_vehicletypereliability
                    uint32                p_hasdownbody
                    uint32                p_hasdownbodyreliability
                    uint32                p_posture
                    uint32                p_posturereliability
                    uint32                p_haserrordetect
                    uint32                p_uniformstyle
                    uint32                p_uniformstylereliability
                    uint32                p_hasraincoat
                    uint32                p_hasraincoatreliability
                    uint32                p_agebracket
                    uint32                p_agebracketreliability
                    uint32                p_gender
                    uint32                p_genderreliability
                    uint32                p_hatstyle
                    uint32                p_hatstylereliability
                    uint32                p_bagtype
                    uint32                p_bagtypereliability
                    uint32                p_upperbodyclothes
                    uint32                p_upperbodyclothesreliability
                    uint32                p_upperbodyclothestype
                    uint32                p_upperbodyclothestypereliability
                    uint32                p_upperbodycolor
                    uint32                p_upperbodycolorreliability
                    uint32                p_upperbodyvein
                    uint32                p_upperbodyveinreliability
                    uint32                p_hairstyle
                    uint32                p_hairstylereliability
                    uint32                p_haircolor
                    uint32                p_haircolorreliability
                    uint32                p_downperbodyclothes
                    uint32                p_downperbodyclothesreliability
                    uint32                p_downperbodycolor
                    uint32                p_downperbodycolorreliability
                    uint32                p_downperbodyvein
                    uint32                p_downperbodyveinreliability
                    string                p_algorithmversion
                    numpy.array           p_featuredata
                    double                p_gps_x
                    double                p_gps_y
                    sint32                p_track_id
                    float                 p_iqascore
                    uint32                p_haspicinfrared
                    uint32                p_nonmotorumbrellatype
                    uint32                p_nonmotorumbrellatypereliability
                    uint32                p_body_num
                    uint32                p_is_related_face
                    uint32                p_head_score
                    uint32                p_upbody_score
                    uint32                p_downbody_score
        
                    support asynchronous
        """
    def exclude(self, arg0: list[str]) -> pic_info:
        """
                从抓拍集中去除输入的rids
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb_1 = db.get_partition("0-0")
        
                it = db.get_time_it(0)
                pb_2 = it.get(256)
        
                pb = pb_1.exclude(pb_2)
                
                print(pb_1, pb_2)
                print(pb)
                ```
                support asynchronous
        """
    def feature_set_enhancement(self, low: float = -0.5, high: float = 0.5) -> None:
        """
                通过给特征增加随机值的方式对特征数据进行扩增，得到一个新抓拍集
                support asynchronous
        """
    def filter_from_level(self, lower: int, upper: int) -> pic_info:
        """
                根据分数上下限获取分级后符合条件的抓拍，左闭右开
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
        
                alg = pycluster.cluster_hdl([pycluster.FACE, pycluster.BODY], pycluster.default_cfg())      # 通过cluster_hdl创建参数为默认参数的算法句柄alg
                pb = pycluster_sql.pb_input_sql("0-0")                                                      # 从数据库读取0-0分区的数据pb
                pb.get_level(alg)                                                                           # 对数据pb分级
                illegal = pb.filter_from_level(-127, 0)                                                             # 等级处于[-127, 0)的所有数据认定为废片illegal
                ```
                support asynchronous
        """
    def get_feature(self) -> dict[pycluster2x.lib.pycluster.mdl_e, numpy.ndarray[numpy.float32]]:
        """
                输入算法句柄，将抓拍分级，获取分数
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
        
                alg = pycluster.cluster_hdl([pycluster.FACE, pycluster.BODY], pycluster.default_cfg())      # 通过cluster_hdl创建参数为默认参数的算法句柄alg
                pb = pycluster_sql.pb_input_sql("0-0")                                                      # 从数据库读取0-0分区的数据pb
                pb.get_level(alg)                                                                           # 对数据pb分级
                illegal = pb.get_level(-127, 0)                                                             # 等级处于[-127, 0)的所有数据认定为废片illegal
                ```
        """
    def get_feature_as_view(self) -> pic_info.pic_feature_viewer_t:
        """
                同 get_feature ，获取特征，但是和dossier共享同一块内存，对特征的修改会同步
                通过入口函数保证对象的生命周期内特征有效
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                pics = pypic.pb_input_csv(f"{current_dir}/data1.csv")
                with pics.get_feature_as_view() as ftr:
                    # dict[pycluster2x.lib.pycluster.mdl_e, numpy.ndarray[numpy.float32]]
                    #     [模态][第m张抓拍][dim维中的第k个数字]
                    ftr[pycluster.FACE][0][0] = 0.2
                ```
        """
    def get_ftr(self) -> dict[pycluster2x.lib.pycluster.mdl_e, numpy.ndarray[numpy.float32]]:
        """
                输入算法句柄，将抓拍分级，获取分数
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
        
                alg = pycluster.cluster_hdl([pycluster.FACE, pycluster.BODY], pycluster.default_cfg())      # 通过cluster_hdl创建参数为默认参数的算法句柄alg
                pb = pycluster_sql.pb_input_sql("0-0")                                                      # 从数据库读取0-0分区的数据pb
                pb.get_level(alg)                                                                           # 对数据pb分级
                illegal = pb.get_level(-127, 0)                                                             # 等级处于[-127, 0)的所有数据认定为废片illegal
                ```
        """
    @typing.overload
    def get_level(self, alg: pycluster2x.lib.pycluster.cluster_hdl) -> None:
        """
                输入算法句柄，将抓拍分级，获取分数
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
        
                alg = pycluster.cluster_hdl([pycluster.FACE, pycluster.BODY], pycluster.default_cfg())      # 通过cluster_hdl创建参数为默认参数的算法句柄alg
                pb = pycluster_sql.pb_input_sql("0-0")                                                      # 从数据库读取0-0分区的数据pb
                pb.get_level(alg)                                                                           # 对数据pb分级
                illegal = pb.get_level(-127, 0)                                                             # 等级处于[-127, 0)的所有数据认定为废片illegal
                ```
                support asynchronous
        """
    @typing.overload
    def get_level(self, lower: int, upper: int) -> pic_info:
        """
                根据分数上下限获取分级后符合条件的抓拍，左闭右开
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
        
                alg = pycluster.cluster_hdl([pycluster.FACE, pycluster.BODY], pycluster.default_cfg())      # 通过cluster_hdl创建参数为默认参数的算法句柄alg
                pb = pycluster_sql.pb_input_sql("0-0")                                                      # 从数据库读取0-0分区的数据pb
                pb.get_level(alg)                                                                           # 对数据pb分级
                illegal = pb.get_level(-127, 0)                                                             # 等级处于[-127, 0)的所有数据认定为废片illegal
                ```
                support asynchronous
        """
    def get_rids(self) -> dict[pycluster2x.lib.pycluster.mdl_e, list[str]]:
        """
                获取抓拍集中的所有rid
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                it = db.get_time_it(0)
                pb = it.get(256)
        
                print(pb.get_rids())
                ```
        """
    def get_rids_level(self) -> dict[pycluster2x.lib.pycluster.mdl_e, dict[str, int]]:
        """
                获取rid和level的表
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
        
                alg = pycluster.cluster_hdl([pycluster.FACE, pycluster.BODY], pycluster.default_cfg())      # 通过cluster_hdl创建参数为默认参数的算法句柄alg
                pb = pycluster_sql.pb_input_sql("0-0")                                                      # 从数据库读取0-0分区的数据pb
                pb.get_level(alg)                                                                           # 对数据pb分级
                illegal = pb.get_level(-127, 0)                                                             # 等级处于[-127, 0)的所有数据认定为废片illegal
                print(illegal.get_rids_level())
                ```
        """
    def get_space_info(self) -> dict[pycluster2x.lib.pycluster.mdl_e, list[sp_info]]:
        """
                获取抓拍集中的所有rid
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                it = db.get_time_it(0)
                pb = it.get(256)
        
                print(pb.get_space_info())
                ```
        """
    def include(self, arg0: list[str]) -> pic_info:
        """
                取抓拍集和输入rids的交集
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb_1 = db.get_partition("0-0")
        
                it = db.get_time_it(0)
                pb_2 = it.get(256)
        
                pb = pb_1.include(pb_2)
                
                print(pb_1, pb_2)
                print(pb)
                ```
                support asynchronous
        """
    @typing.overload
    def person_num(self) -> int:
        """
                获取抓拍集的总人数（抓拍次数，关联的算一次）
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb = db.get_partition("0-0")
        
                print(pb, pb.person_num())
                ```
        """
    @typing.overload
    def person_num(self, arg0: pycluster2x.lib.pycluster.mdl_e) -> int:
        """
                获取输入对应模态的抓拍数
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb = db.get_partition("0-0")
        
                print(pb, pb.person_num(pycluster.FACE), pb.person_num(pycluster.BODY))
                ```
        """
    def person_num_mdl(self) -> dict[pycluster2x.lib.pycluster.mdl_e, int]:
        """
                获取每个模态的抓拍数
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb = db.get_partition("0-0")
        
                print(pb, pb.person_num_mdl())
                ```
        """
    def ser(self) -> bytes:
        """
                序列化，返回python中的bytes数组
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                it = db.get_time_it(0)
                pb = it.get(256)
        
                pb_bytes = pb.ser()
                pb_2 = pypic.unser(pb_bytes)
        
                print(pb, pb_2)
                ```
                support asynchronous
        """
    @typing.overload
    def split(self) -> list[pic_info]:
        """
                根据分区来切割抓拍集数据，每个分区返回一个档案集
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb_1 = db.get_partition("0-0")
                pb_2 = db.get_partition("0-1")
                
                print(pb_1, pb_2)
        
                pb_info = pb_1 + pb_2
                for pb in pb_info.split():
                    print(pb)
                ```
                support asynchronous
        """
    @typing.overload
    def split(self, mode: str) -> list[pic_info]:
        """
                模式字符串填"gender"时通过性别把包含人脸的抓拍分开，不含人脸的抓拍单独分开，最后成为3个抓拍集
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb_1 = db.get_partition("0-0")
                
                for pb in pb_info.split("gender"):
                    print(pb)
                ```
                support asynchronous
        """
    @typing.overload
    def split(self, num: int) -> list[pic_info]:
        """
                根据分区的数量要求，把分区分为入参数量个独立抓拍集，每个抓拍集的抓拍都根据gps临近关系均匀划分
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
        
                pb_1 = db.get_partition("0-0")
                
                for pb in pb_info.split(10000):
                    print(pb)
                ```
                support asynchronous
        """
class sp_info:
    """
    时空信息
    """
    def channel_code(self) -> str:
        """
                获取gps
        """
    def gps(self) -> tuple[float, float]:
        """
                获取gps
        """
    def time(self) -> int:
        """
                获取实际戳
        """
def async_pb_input_csv(csv_path: str) -> pic_info:
    """
    
    async function of
    pb_input_csv(csv_path: str) -> pycluster2x.lib.pypic.pic_info
        
    """
def async_unser(arg0: str) -> pic_info:
    """
    
    async function of
    unser(arg0: str) -> pycluster2x.lib.pypic.pic_info
        
    """
def doc() -> None:
    ...
def pb_input_csv(csv_path: str) -> pic_info:
    """
            从csv获取抓拍集
            support asynchronous
    """
def unser(arg0: str) -> pic_info:
    """
            通过bytes数组反序列化
            support asynchronous
    """
