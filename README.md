# Web UI 自动化测试项目

## 一、项目简介

本项目是一个基于 Python + Selenium + Pytest 搭建的 Web UI 自动化测试项目，主要覆盖用户登录、登录失败提示、商品加入购物车、商品移除购物车等常见 Web 测试场景。

项目采用 Page Object 分层设计，将页面元素定位、页面操作和测试用例进行拆分，提高代码复用性和维护性，并支持生成 Allure 测试报告，方便查看测试执行结果。

---

## 二、技术栈

- Python
- Selenium
- Pytest
- Allure
- Git / GitHub
- PyCharm

---

## 三、项目结构

```text
web_auto_project/
├── config/
│   └── config.py             # 项目配置文件，管理测试网站地址
├── pages/
│   ├── login_page.py         # 登录页面封装
│   └── product_page.py       # 商品页面封装
├── screenshots/              # 测试失败截图目录
├── testcases/
│   └── test_login.py         # 登录相关测试用例
├── conftest.py               # Pytest 公共前置 fixture
├── README.md                 # 项目说明文档
├── report.html               # pytest-html 测试报告
└── .gitignore                # Git 忽略文件
```

---

## 四、主要测试场景

| 模块 | 测试场景 | 验证点 |
|---|---|---|
| 登录模块 | 正确用户名和密码登录 | 是否成功进入商品列表页 |
| 登录模块 | 错误用户名或密码登录 | 是否展示登录失败提示 |
| 商品模块 | 登录后进入商品列表页 | 商品页面是否正常展示 |

---

## 五、运行方式

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

### 2. 运行测试用例

```bash
pytest testcases -s
```

### 3. 生成 Allure 原始测试结果

```bash
pytest testcases -s --alluredir=allure-results
```

### 4. 打开 Allure 测试报告

```bash
allure serve allure-results
```

---

## 六、测试报告

项目支持使用 Allure 生成可视化测试报告，可以查看测试用例执行结果、失败原因、执行时间和测试步骤信息。

---

## 七、后续优化方向

- 增加结算流程、订单提交流程等业务场景
- 增加数据驱动测试，提高测试覆盖率
- 增加失败截图机制，方便定位页面问题
- 增加日志封装，记录关键测试步骤
- 后续可结合 Jenkins 实现自动化测试持续集成