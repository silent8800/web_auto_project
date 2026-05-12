# Web UI 自动化测试项目

## 一、项目简介

本项目是一个基于 Python + Selenium + Pytest 搭建的 Web UI 自动化测试项目，主要覆盖用户登录、登录失败提示、商品页面访问等常见 Web 测试场景。

项目采用 Page Object 分层设计，将页面元素定位、页面操作和测试用例进行拆分，提高代码复用性和维护性。同时项目支持生成 pytest-html 和 Allure 测试报告，并封装了失败自动截图功能，方便定位自动化测试失败原因。

---

## 二、技术栈

- Python
- Selenium
- Pytest
- pytest-html
- Allure
- Git / GitHub

---

## 三、项目结构

```text
web_auto_project/
├── config/
│   └── config.py             # 项目配置文件，管理测试网站地址
├── pages/
│   ├── login_page.py         # 登录页面封装
│   └── product_page.py       # 商品页面封装
├── screenshots/
│   └── .gitkeep              # 失败截图目录占位文件
├── testcases/
│   └── test_login.py         # 登录相关测试用例
├── conftest.py               # Pytest 公共前置 fixture
├── requirements.txt          # 项目依赖文件
├── report.html               # pytest-html 测试报告
├── README.md                 # 项目说明文档
└── .gitignore                # Git 忽略文件
```

---

## 四、主要测试场景

| 模块 | 测试场景 | 验证点 |
|---|---|---|
| 登录模块 | 正确用户名和密码登录 | 是否成功进入商品列表页 |
| 登录模块 | 错误用户名或密码登录 | 是否展示登录失败提示 |
| 商品模块 | 登录后访问商品页面 | 商品页面是否正常展示 |

---

## 五、项目特点

- 使用 Selenium 模拟用户在浏览器中的真实操作
- 使用 Pytest 管理和执行自动化测试用例
- 使用 Page Object 思想封装页面元素和页面操作
- 使用 `conftest.py` 管理浏览器启动和关闭等公共前置
- 支持用例失败自动截图，并保存到 `screenshots/` 目录
- 支持生成 pytest-html 和 Allure 测试报告

---

## 六、运行方式

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试用例

```bash
pytest testcases -s
```

### 3. 生成 pytest-html 测试报告

```bash
pytest testcases -s --html=report.html --self-contained-html
```

### 4. 生成 Allure 原始测试结果

```bash
pytest testcases -s --alluredir=allure-results
```

### 5. 打开 Allure 测试报告

```bash
allure serve allure-results
```

---

## 七、测试报告说明

项目支持生成 pytest-html 和 Allure 测试报告，用于查看测试用例执行结果、失败原因和执行时间。

同时项目在 `conftest.py` 中封装了失败自动截图功能：

- 当测试用例执行失败时，自动保存当前页面截图到 `screenshots/` 目录
- 失败截图会自动附加到 Allure 报告中
- 方便定位页面跳转失败、元素定位失败或断言失败等问题

---

## 八、后续优化方向

- 增加购物车、结算流程等业务场景测试用例
- 增加数据驱动测试，提高测试覆盖率
- 增加日志封装，记录关键测试执行信息
- 后续可结合 Jenkins 实现自动化测试持续集成