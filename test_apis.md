
# 项目API操作说明
## 一、单接口测试
## 数据来源：coupon_data_xlsx，XH/data/coupon_data_xlsx,sheet_name:添加优惠券接口
## 测试数据对应：casename(测试用例名称),category(优惠券类型),expect_status(状态码)。。。。（可根据实际业务进行添加）
## 注意：parametrize和params需保持一致，否则会报错
## excel表格
```python
class test_coupon_now:
    test_data = read_excel(coupon_data_xlsx, '添加优惠券接口')
    @allure.title('添加优惠券excel')
    @pytest.mark.parametrize('casename,category,expect_status', test_data)
    def test_coupon_now2(self,casename,category,expect_status):
        allure.dynamic.title(casename)
        api = ManagerCouponAddApi(category=category)
        resp = api.send()
        pytest.assume(resp.status_code==expect_status,f'期望值:{expect_status},实际值:{resp.status_code}')
        pytest.assume(resp.json().get('code')==200,f'期望值:{200},实际值:{resp.json().get("code")}')
```
##  yaml格式
```python
class test_coupon_now2:
    test_data = load_yaml_file(mtxshop_data_yaml)['添加优惠券接口']
    @allure.title('添加优惠券xml')
    @pytest.mark.parametrize('casename,category,new_params,expect_status,expect_body', test_data)
    def test_coupon_now1(self,casename,category,new_params,expect_status,expect_body):
        allure.dynamic.title(casename)
        api = ManagerCouponAddApi(category=category)or json_path, new_value in new_params.items():
        resp = api.send()
        pytest.assume(resp.status_code==expect_status,f'期望值:{expect_status},实际值:{resp.status_code}')
        pytest.assume(resp.text == expect_body, f'期望值:{expect_body},实际值:{resp.text}')
```
### 场景：
### 梳理出对应场景，例如：1、添加优惠券 2、查询优惠券 3、更改优惠券状态 4、删除优惠券
### 梳理出对应的接口，找到接口之间的依赖关系例如：更改优惠券状态接口依赖添加优惠券接口，添加完成之后再更改，删除优惠券接口依赖添加优惠券接口，添加完成之后再删除
### 再进行代码编写，并调试运行

```python
class TestOrderFlow:
    coupon_close = 0  # 优惠券状态 -关闭
    coupon_open = 1  # 优惠券状态 -开启
    coupon_id = ''  # 优惠券ID
   
    @allure.title('添加优惠券')
    @pytest.mark.dependency()
    def test_coupon_now(self):
        # 添加优惠券
        resp = ManagerCouponAddApi(category=7).send()
        assert resp.status_code == 200
        # 获取优惠券id
        list_resp = ManagerCouponListApi().send()
        TestOrderFlow.coupon_id = jsonpath.jsonpath(list_resp.json(), '$..list[0].id')[0]
        pytest.assume(resp.status_code == 200, f'期望值:200,实际值:{resp.status_code}')

    @allure.title('关闭优惠券')
    @pytest.mark.dependency(depends=['TestOrderFlow::test_coupon_now'])
    def test_coupon_close(self, db_init):
        ManagerCouponCloseApi(TestOrderFlow.coupon_id).send()
        # 优化SQL查询，使用参数化查询避免SQL注入，确保在mall数据库中查询eb_coupon表
        res = db_init.select('SELECT * FROM eb_coupon WHERE id = %s LIMIT 1', (TestOrderFlow.coupon_id,))
        # 提取数据库查询出status列的值并与预期值进行比较
        assert TestOrderFlow.coupon_close == res[0]['status'], '优惠券状态一致'
        print(f'优惠券状态:{TestOrderFlow.coupon_close}，res是{res[0]['status']}')
        if res and len(res) > 0:
            TestOrderFlow.coupon_close = res[0]['status']
        else:
            print(f'未找到ID为 {TestOrderFlow.coupon_id} 的优惠券记录')
```
### 总结场景测试，核心要点
### 依赖
### 1、依赖，B接口依赖A接口的返回值，通过设置类属性，进行传递
### 2、接口依赖，B接口依赖A接口，通过装饰器@pytest.mark.dependency(depends=['类名::依赖方法名'])
### 断言
### 1、使用pytest.assume进行断言,支持从数据库（db_init）、redis（redis_init）、response获取数据进行断言
### 数据处理
### 1、使用update_value_to_json进行数据处理，增删改json
```python

def update_value_to_json():
    pass
json_object = {"goods_name":"水杯","goods_gallery_list":[{"sort":0,"img_url":"http://192.168.1.100:8080/group1/M00/00/00/rBHu8l_xKvKAQqjXAAAjZ5_Q5_E.png"}]}
#参数为空
json_object = update_value_to_json(json_object,'$.goods_name','')
#修改
json_object = update_value_to_json(json_object,'$.goods_gallery_list[0].sort',1)
#删除
json_object = update_value_to_json(json_object,'$.goods_name','$del')
#追加
json_object = update_value_to_json(json_object, add_new={"new_field": "new_value", "another_field": "another_value"})
```

