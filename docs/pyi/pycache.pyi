from __future__ import annotations
import pycluster2x.lib.pycluster
import pycluster2x.lib.pypic
import typing
__all__ = ['abstract_database', 'cluster_data_cache', 'db_it']
class abstract_database:
    """
    缓存抽象类
    """
    def __init__(self) -> None:
        ...
    def contains_partition(self, partition: str) -> bool:
        ...
    def data_count(self) -> int:
        ...
    def from_partition(self, partition: str) -> list[dict[str, str]]:
        ...
    def from_rid(self, rid: str, e: pycluster2x.lib.pycluster.mdl_e) -> list[dict[str, str]]:
        ...
    def from_rids(self, rids: list[str], e: pycluster2x.lib.pycluster.mdl_e) -> list[dict[str, str]]:
        ...
    def get(self, idx: int, size: int = 1) -> list[dict[str, str]]:
        ...
    def size(self) -> int:
        ...
class cluster_data_cache:
    """
    
            数据缓存类，每个demo都包含一个静态的本地数据缓存，可以通过：
            例如：
            ``` python
    
            db:pycache.cluster_data_cache = pycache.local_data_cache()
            ```
            获取demo自身的静态本地数据缓存
            除此以外，还可以根据数据缓存地址，打开其他的数据缓存：
            例如：
            ``` python
    
            db_other = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")
            ```
        
    """
    def __contains__(self, arg0: str) -> bool:
        """
                判断是否包含分区名为入参的分区：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                if db.contains("0-0"):                                # 判断数据缓存是否包含"0-0"分区
                    it:pycache.db_it = db.get_partition_it("0-0")      # 根据分区号，获取该分区时间戳最早的数据迭代器
                    pb_info_1:pypic.pic_info = it.get(256)                      # 从迭代器获取最多256张抓拍
                    print("pic count:", pb_info_1)
                ```
        """
    def __init__(self, arg0: str) -> None:
        ...
    def async_from_rid(self, *args, **kwargs):
        """
        
        async function of
        from_rid(self: pycluster2x.lib.pycache.cluster_data_cache, rid: str) -> pycluster2x.lib.pypic.pic_info
        from_rid(self: pycluster2x.lib.pycache.cluster_data_cache, mdl: pycluster2x.lib.pycluster.mdl_e, rid: str) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_from_rids(self, mdl: pycluster2x.lib.pycluster.mdl_e, rids: list[str]) -> pycluster2x.lib.pypic.pic_info:
        """
        
        async function of
        from_rids(self: pycluster2x.lib.pycache.cluster_data_cache, mdl: pycluster2x.lib.pycluster.mdl_e, rids: list[str]) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_get(self, *args, **kwargs):
        """
        
        async function of
        get(self: pycluster2x.lib.pycache.cluster_data_cache, begin: int) -> pycluster2x.lib.pypic.pic_info
        get(self: pycluster2x.lib.pycache.cluster_data_cache, begin: int, count: int) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_get_partition(self, partition: str) -> pycluster2x.lib.pypic.pic_info:
        """
        
        async function of
        get_partition(self: pycluster2x.lib.pycache.cluster_data_cache, partition: str) -> pycluster2x.lib.pypic.pic_info
            
        """
    def async_save(self, pb_input: pycluster2x.lib.pypic.pic_info, partition: str = '') -> None:
        """
        
        async function of
        save(self: pycluster2x.lib.pycache.cluster_data_cache, pb_input: pycluster2x.lib.pypic.pic_info, partition: str = '') -> None
            
        """
    def big_partition_list(self) -> list[str]:
        """
                获取数据缓存所有大分区形成的列表：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                print("big_partition_list:", db.big_partition_list())
                ```
        """
    def contains(self, arg0: str) -> bool:
        """
                判断是否包含分区名为入参的分区：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                if db.contains("0-0"):                                # 判断数据缓存是否包含"0-0"分区
                    it:pycache.db_it = db.get_partition_it("0-0")      # 根据分区号，获取该分区时间戳最早的数据迭代器
                    pb_info_1:pypic.pic_info = it.get(256)                      # 从迭代器获取最多256张抓拍
                    print("pic count:", pb_info_1)
                ```
        """
    def db_data_num(self) -> tuple[int, int, int]:
        """
                获取数据缓存中的总数据量：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
                print(db.db_data_num())
                ```
        """
    def db_write_down(self) -> None:
        """
                当抓拍集写入数据缓存后调用此函数更新数据缓存文件：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
                db.db_write_down()
                ```
                一般不需要调用
        """
    @typing.overload
    def from_rid(self, rid: str) -> pycluster2x.lib.pypic.pic_info:
        """
                按照record id 获取数据
                support asynchronous
        """
    @typing.overload
    def from_rid(self, mdl: pycluster2x.lib.pycluster.mdl_e, rid: str) -> pycluster2x.lib.pypic.pic_info:
        """
                按照record id 获取数据
                support asynchronous
        """
    def from_rids(self, mdl: pycluster2x.lib.pycluster.mdl_e, rids: list[str]) -> pycluster2x.lib.pypic.pic_info:
        """
                按照record id 获取数据
                support asynchronous
        """
    @typing.overload
    def get(self, begin: int) -> pycluster2x.lib.pypic.pic_info:
        """
                获得数据缓存中按存储顺序排列的第n条数据
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                print(db.get(5))
                ```
                support asynchronous
        """
    @typing.overload
    def get(self, begin: int, count: int) -> pycluster2x.lib.pypic.pic_info:
        """
                从第begin条数据开始，获得数据缓存中按存储顺序排列的count条数据
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存  
        
                print(db.get(100, 5))
                ```
                如果n大于数据总数会抛出c++异常
                support asynchronous
        """
    def get_partition(self, partition: str) -> pycluster2x.lib.pypic.pic_info:
        """
                按分区名字获取一个分区的所有数据
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                if db.contains("0-0"):
                    pb = db.get_partition("0-0")
                ```
                如果获取的分区名不存在，会抛出c++异常
                support asynchronous
        """
    def get_time_it(self, arg0: int) -> db_it:
        """
                根据时间戳获取一个抓拍数据迭代器：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
                it:pycache.db_it = db.get_time_it(0)               # 根据时间流，从时间流最开始，获取时间流最初的数据迭代器
                pb_info_1:pypic.pic_info = it.get(256)                      # 从迭代器获取256张图，组成图片集，迭代器往后移动256张图
                ```
        """
    def keys(self) -> list[str]:
        """
                获取数据缓存可能包含的所有的键：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                print("keys:", db.keys())
                ```
        """
    def partition_list(self) -> list[str]:
        """
                获取数据缓存所有分区形成的列表：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                print("partition_list:", db.partition_list())
                ```
        """
    def save(self, pb_input: pycluster2x.lib.pypic.pic_info, partition: str = '') -> None:
        """
                抓拍将数据保存到数据缓存
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                if not db.contains("0-0"):
                    pb = pycluster_sql.pb_input_sql("0-0")          # 从数据服务下载分区号为"0-0"的抓拍集数据
                    db.save(pb, "0-0")                              # 把该抓拍集保存到数据缓存中
                ```
                support asynchronous
        """
    def size(self) -> int:
        """
                获得数据缓存中储存的总数据量
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                print(db.size())
                ```
        """
    def small_partition_list(self, arg0: str) -> list[str]:
        """
                获取数据缓存某个大分区包含的小分区列表：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
        
                print("small_partition_list:", db.small_partition_list())
                ```
        """
class db_it:
    """
    抓拍数据迭代器类
    """
    __hash__: typing.ClassVar[None] = None
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: db_it) -> bool:
        ...
    def __init__(self) -> None:
        ...
    def __ne__(self, arg0: db_it) -> bool:
        ...
    def __str__(self) -> str:
        ...
    @typing.overload
    def get(self) -> pycluster2x.lib.pypic.pic_info:
        """
                获取一张抓拍，迭代器迭代
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
                it:pycache.db_it = db.get_time_it(0)               # 根据时间流，从时间流最开始，获取时间流最初的数据迭代器
                pb_info_1:pypic.pic_info = it.get()                         # 从迭代器获取1张抓拍，组成抓拍集，迭代器往后移动1张
                pb_info_2:pypic.pic_info = it.get()                         # 从迭代器获取1张抓拍，组成抓拍集，迭代器往后移动1张
                ```
                上述代码从"/data/291223/data/data_cache_ah/"数据缓存中，获取了数据缓存按时间排列的第一张抓拍和第二张抓拍，分别组成抓拍集对象pb_info_1和pb_info_2
                （关联的一组人脸人体抓拍算一张）
        """
    @typing.overload
    def get(self, arg0: int) -> pycluster2x.lib.pypic.pic_info:
        """
                获取若干张抓拍，迭代器迭代
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
                it:pycache.db_it = db.get_time_it(0)               # 根据时间流，从时间流最开始，获取时间流最初的数据迭代器
                pb_info_1:pypic.pic_info = it.get(256)                      # 从迭代器获取256张图，组成抓拍集，迭代器往后移动256张
                ```
                上述代码从"/data/291223/data/data_cache_ah/"数据缓存中，获取了数据缓存按时间排列的前256张图
                （关联的一组人脸人体抓拍算一张）
        """
    @typing.overload
    def get(self, count: int, *, time_upperbound: int) -> pycluster2x.lib.pypic.pic_info:
        """
                获取若干张抓拍，要求时间范围不超过time_upperbound，迭代器迭代
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存 
                it:pycache.db_it = db.get_time_it(0)               # 根据时间流，从时间流最开始，获取时间流最初的数据迭代器
                time_upperbound = it.time() + 100                           # 获取截至时间戳不超过第一张抓拍时间戳+100秒
                pb_info_1:pypic.pic_info = it.get(256, time_upperbound=time_upperbound) # 从迭代器获取最多256张不超过截止时间戳time_upperbound的抓拍数据
                print("pic count:", pb_info_1)
                ```
                由于截至时间戳的存在，实际不超过截止时间戳的抓拍数可能不到256，所以print显示的抓拍数不一定为256
                （关联的一组人脸人体抓拍算一张）
        """
    def not_end(self) -> bool:
        """
                检查迭代器是否已结束
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存   
                it:pycache.db_it = db.get_time_it(0)               # 根据时间流，从时间流最开始，获取时间流最初的数据迭代器
                
                while it.not_end():
                    it.get()
                ```
                上述代码通过一个数据缓存的时间迭代器，遍历了数据缓存里的所有数据
                一般情况，可以直接使用 pycache.db_it.__bool__ 运算符代替此函数:
                例如：
                ``` python
        
                while it:
                    it.get()
                ```
        """
    def time(self) -> int:
        """
                获取当前迭代器数据的时间戳：
                例如：
                ``` python
        
                from pycluster2x import pycluster, pydossier, pypic, pycache
                db = pycache.cluster_data_cache("/data/291223/data/data_cache_ah/")      # 初始化数据缓存
                it:pycache.db_it = db.get_time_it(0)               # 根据时间流，从时间流最开始，获取时间流最初的数据迭代器
        
                print('time', it.time())
                ```
        """
