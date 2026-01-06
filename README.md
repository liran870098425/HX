# HX自动化测试框架

HX是一个基于Python的自动化测试框架，专门用于API接口测试。项目集成了数据驱动测试、参数化测试、Allure报告生成等功能，支持对单接口进行灵活的测试用例设计和执行。

## 项目特性

### 1. 数据驱动测试
- 支持Excel和YAML格式的测试数据文件
- 测试数据与测试逻辑完全分离
- 通过[file_load.py](file:///C:%5CUsers%5CAdministrator%5CPycharmProjects%5CHX%5Ccommon%5Cfile_load.py)模块自动加载和解析测试数据
- 使用pytest的parametrize功能实现参数化测试

### 2. 单接口测试
- 每个API接口封装为独立的类，便于管理和调用
- 支持动态构建HTTP请求（URL、请求头、请求体等）
- 支持对响应状态码、响应体、响应头等进行断言验证
- 提供完整的接口测试解决方案

### 3. 参数动态修改功能
项目核心功能，支持对请求参数进行动态的增删改操作：

#### 3.1 参数修改机制
- **核心工具**：[common/json_util.py](file:///C:%5CUsers%5CAdministrator%5CPycharmProjects%5CHX%5Ccommon%5Cjson_util.py)中的[update_value_to_json](file:///C:%5CUsers%5CAdministrator%5CPycharmProjects%5CHX%5Ccommon%5Cjson_util.py#L13-L32)方法
- **核心技术**：使用jsonpath-ng库解析JSON路径表达式
- **工作原理**：通过JSONPath定位到目标参数，然后执行相应的修改操作

#### 3.2 参数修改类型
- **更新操作**：修改指定路径的参数值
  - 通过[json_path](file:///C:%5CUsers%5CAdministrator%5CPycharmProjects%5CHX%5Capi%5Cbase_api.py#L35-L35)参数定位目标字段
  - 使用[new_value](file:///C:%5CUsers%5CAdministrator%5CPycharmProjects%5CHX%5Capi%5Cbase_api.py#L46-L46)参数提供新值
  - 支持嵌套对象、数组元素的更新

- **删除操作**：删除指定路径的参数
  - 使用特殊值"$del"作为[new_value](file:///C:%5CUsers%5CAdministrator%5CPycharmProjects%5CHX%5Capi%5Cbase_api.py#L46-L46)参数
  - 支持删除普通字段、嵌套字段和数组元素

- **新增操作**：向JSON对象添加新参数
  - 使用[add_new](file:///C:%5CUsers%5CAdministrator%5CPycharmProjects%5CHX%5Ctestcase%5CManager_case%5Ctest_coupon_case.py#L25-L25)参数传递要添加的键值对字典
  - 支持同时添加多个新字段

### 4. JSONPath参数定位
- 支持标准JSONPath语法（如$.field、$.array[0]、$.nested.field等）
- 支持多层嵌套对象的参数定位
- 支持数组元素的定位和修改

### 5. 测试数据管理
- YAML数据文件：存储结构化测试数据
- Excel数据文件：支持表格形式的测试数据
- 自动加载和解析不同格式的数据文件
- 根据加载的数据自动执行多组测试

### 6. 报告生成与展示
- 集成Allure报告系统
- pytest-allure插件自动收集测试执行数据
- 生成详细的HTML格式测试报告
- 支持在浏览器中查看和分析测试结果

### 7. 配置管理
- 支持SIT、UAT、TEST等多环境配置
- 支持运行时动态切换环境配置
- 自动加载对应环境的配置信息

## 项目结构
```
.
├── allure/                 # Allure命令行工具
│   └── allure-2.24.0/      # Allure具体版本目录
├── allure-results/         # Allure测试结果（pytest-allure插件默认输出目录）
├── api/                    # API接口定义
│   ├── Buyer/             # 买家相关接口
│   ├── Manager/           # 管理端相关接口
│   └── Merchant/          # 商家相关接口
├── common/                 # 公共模块
│   ├── client.py          # HTTP客户端
│   ├── json_util.py       # JSON处理工具
│   ├── logger.py          # 日志工具
│   └── ...                # 其他公共模块
├── config/                 # 配置文件
├── data/                   # 测试数据
├── report/                 # 测试报告
│   ├── data/              # Allure报告原始数据
│   └── html/              # 生成的HTML报告
├── testcase/               # 测试用例
├── conftest.py            # pytest配置
├── pytest.ini             # pytest配置文件
├── requirements.txt       # 依赖包列表
├── run.py                 # 测试执行入口
└── README.md              # 项目说明文档
```

## 技术栈
- **编程语言**：Python 3.x
- **测试框架**：pytest
- **HTTP客户端**：requests
- **JSON处理**：jsonpath-ng
- **报告工具**：Allure
- **数据格式**：YAML、Excel
- **日志系统**：Python logging

## 快速开始

### 1. 环境准备
```bash
# 安装依赖
pip install -r requirements.txt

# 确保Allure命令行工具已安装并配置到PATH
```

### 2. 运行测试
```bash
# 方式1：直接运行
python run.py

# 方式2：使用pytest命令
pytest testcase/ -sv --alluredir=report/data --clean-alluredir
```

### 3. 生成报告
```bash
# 生成HTML报告
allure generate report/data -o report/html --clean
allure open report/html
```

## 项目特点
1. **高扩展性**：模块化设计，便于功能扩展
2. **易维护性**：数据与代码分离，便于维护
3. **灵活性**：支持多种参数操作方式
4. **自动化**：完整的自动化测试流程
5. **可视化**：详细的测试报告和执行结果

## 使用场景
- API接口自动化测试
- 接口回归测试
- 接口性能测试
- 接口安全测试
- 数据驱动的接口测试
- 多环境接口验证

## 文档
- [PROJECT_STRUCTURE.md](PROJECT_STRUCTURE.md) - 详细项目结构说明
- [HX项目结构说明.docx](HX项目结构说明.docx) - 项目结构详细文档