---
type: "playbook"
status: "active"
created: "2026-05-28"
updated: "2026-05-28"
sources:
  - "https://docs.python.org/zh-cn/3/tutorial/"
  - "https://docs.python.org/3/tutorial/"
  - "https://docs.python.org/3/library/"
  - "https://docs.python.org/3/reference/"
  - "https://packaging.python.org/en/latest/tutorials/packaging-projects/"
  - "https://docs.pytest.org/en/stable/"
  - "https://automatetheboringstuff.com/"
  - "https://realpython.com/"
  - "https://docs.python.org/3/library/asyncio.html"
  - "https://mypy.readthedocs.io/en/stable/getting_started.html"
  - "https://fastapi.tiangolo.com/"
  - "https://docs.djangoproject.com/en/stable/intro/tutorial01/"
  - "https://pandas.pydata.org/docs/getting_started/intro_tutorials/"
  - "https://jakevdp.github.io/PythonDataScienceHandbook/"
tags: ["python", "learning-path", "backend", "automation", "testing"]
---

# 定位

这页用于把 Python 从入门到进阶的学习资料整理成一条可执行路径。目标不是堆链接，而是按能力阶段组织：先能写小脚本，再能写可维护项目，最后进入 Web、数据、自动化、并发和工程化方向。

Python 学习不要只停留在语法题。比较有效的路线是：语法基础 + 标准库 + 文件/网络/数据处理 + 测试 + 包管理 + 类型标注 + 一个具体方向项目。

# 学习路线

## 1. 入门：语法、数据结构和小脚本

目标：能读懂常见 Python 代码，能写 100 行以内的小脚本解决真实问题。

重点：

- 基础语法：变量、条件、循环、函数、模块、异常。
- 内置数据结构：`list`、`tuple`、`dict`、`set`、字符串。
- 文件处理：读写文本、CSV、JSON、路径处理。
- 调试习惯：会用 `print`、断点、异常信息定位问题。

推荐资料：

- [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/)：最稳定的入门主线，适合按章节过一遍。
- [Python 官方教程（英文）](https://docs.python.org/3/tutorial/)：遇到中文翻译不清楚时，对照英文原文。
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)：偏实用脚本，适合把 Python 和日常自动化结合起来。

练习建议：

- 写一个批量重命名文件脚本。
- 写一个 CSV/JSON 转换脚本。
- 写一个从网页或接口拉取数据并保存到本地的脚本。
- 写一个命令行待办、账本或日志统计工具。

## 2. 初级到中级：标准库、项目结构和依赖管理

目标：能把脚本整理成一个可复用的小项目，而不是只写一次性代码。

重点：

- 标准库：`pathlib`、`datetime`、`json`、`csv`、`re`、`subprocess`、`argparse`、`logging`、`venv`。
- 项目结构：模块拆分、入口文件、配置文件、README、示例数据。
- 虚拟环境：每个项目有独立依赖，不污染系统 Python。
- 包管理：理解 `pyproject.toml`、构建、发布和安装的基本流程。

推荐资料：

- [Python Standard Library](https://docs.python.org/3/library/)：查标准库时优先看官方文档。
- [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/)：理解如何把代码组织成可安装项目。

练习建议：

- 把入门阶段的小脚本改成带 `argparse` 的命令行工具。
- 给工具加 `logging`，区分正常输出、调试日志和错误日志。
- 用 `venv` 建独立环境，记录依赖和运行方式。

## 3. 工程化：测试、类型、质量和可维护性

目标：能写出别人接手也能维护的 Python 代码。

重点：

- 测试：单元测试、fixture、临时文件、异常路径、边界条件。
- 类型标注：函数签名、容器类型、`Optional`、`Protocol`、`TypedDict`。
- 代码质量：命名、模块边界、错误处理、重复逻辑收敛。
- 配置与环境：环境变量、配置文件、不同环境的参数隔离。

推荐资料：

- [pytest documentation](https://docs.pytest.org/en/stable/)：Python 测试事实标准之一，适合从简单断言学起。
- [mypy Getting Started](https://mypy.readthedocs.io/en/stable/getting_started.html)：补类型检查和静态分析意识。
- [Real Python](https://realpython.com/)：主题覆盖广，适合查特定概念、库和实践文章；部分内容可能有付费墙。

练习建议：

- 给已有脚本补测试，覆盖正常输入、空输入、错误输入。
- 给核心函数加类型标注，并用 mypy 检查。
- 把网络、文件系统、时间等外部依赖包成可替换接口，降低测试难度。

## 4. 进阶语言能力：迭代器、上下文管理、装饰器和并发

目标：理解 Python 代码背后的运行机制，能读懂框架和库里的常见高级写法。

重点：

- 迭代协议：iterator、generator、`yield`。
- 上下文管理：`with`、context manager、资源释放。
- 装饰器：函数包装、参数保持、常见框架用法。
- 面向对象：dataclass、继承边界、组合优先、协议式抽象。
- 并发模型：threading、multiprocessing、asyncio 的适用边界。

推荐资料：

- [Python Language Reference](https://docs.python.org/3/reference/)：需要确认语义时查这里。
- [asyncio 官方文档](https://docs.python.org/3/library/asyncio.html)：学习异步 IO 的主入口。

练习建议：

- 用 generator 处理大文件，避免一次性读入内存。
- 写一个上下文管理器管理临时目录或数据库连接。
- 用 `asyncio` 写一个并发请求脚本，再和同步版本对比复杂度和收益。

## 5. 方向一：Web 后端

目标：能用 Python 写 API、后台服务或完整 Web 应用。

重点：

- HTTP、路由、请求/响应、参数校验、认证授权。
- ORM、数据库迁移、事务、连接池。
- 后台任务、缓存、队列、日志和部署。
- API 文档、测试和错误处理。

推荐资料：

- [FastAPI](https://fastapi.tiangolo.com/)：适合 API 服务、类型标注驱动开发、自动生成 OpenAPI 文档。
- [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/)：适合学习完整 Web 框架、ORM、后台管理和应用结构。

练习建议：

- 写一个 CRUD API，包含数据库、分页、搜索和错误处理。
- 写认证登录、权限控制和接口测试。
- 把服务部署到本地 Docker 或云服务器，并补日志和健康检查。

## 6. 方向二：数据处理与分析

目标：能用 Python 处理表格数据、日志、指标和简单分析任务。

重点：

- 数据读取：CSV、Excel、JSON、数据库查询结果。
- 数据清洗：缺失值、类型转换、去重、聚合。
- 数据分析：分组统计、时间序列、可视化。
- 输出：报表、图表、导出文件。

推荐资料：

- [pandas Intro Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/)：pandas 官方入门路径。
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)：偏数据科学方向的系统资料，适合后续补 NumPy、pandas、Matplotlib 和机器学习基础。

练习建议：

- 分析一份 CSV 日志，输出日活、留存或错误排行。
- 清洗一份 Excel 数据，生成标准化结果。
- 做一个定时生成报表的小脚本。

# 具体示例与关注点

## 基础语法示例：变量、类型和输出

适合阶段：刚开始学 Python。

目标：理解变量只是名字，值才有类型；先会读懂最基本的表达式和输出。

```python
name = "Sean"
age = 28
height = 1.75
is_active = True

print(name)
print(age + 1)
print(f"{name} is {age} years old")
print(type(height))
```

需要关注：

- Python 变量不需要声明类型，但值本身有类型。
- `=` 是赋值，不是数学等号；右边先计算，再绑定到左边名字。
- `f"{name}"` 是常用字符串格式化方式，比手动拼接更清晰。
- `type()` 适合入门阶段观察值的类型，但真实业务代码不要到处依赖 `type()` 分支。

## 基础语法示例：条件判断

适合阶段：刚开始学 Python。

目标：学会用 `if` 表达分支逻辑。

```python
score = 86

if score >= 90:
    level = "A"
elif score >= 80:
    level = "B"
elif score >= 60:
    level = "C"
else:
    level = "D"

print(level)
```

需要关注：

- Python 用缩进表示代码块，缩进错了逻辑就变了。
- 条件从上往下判断，命中一个分支后不会继续判断后面的 `elif`。
- 比较边界要想清楚，例如 `80`、`90` 这种临界值。
- 简单条件可以直接写，复杂条件要拆成有名字的变量，避免一行里塞太多判断。

## 基础语法示例：循环和累计

适合阶段：刚开始学 Python。

目标：理解 `for` 适合遍历集合，`while` 适合“不知道循环次数”的场景。

```python
numbers = [3, 5, 8, 13]
total = 0

for number in numbers:
    total += number

print(total)
```

需要关注：

- `for number in numbers` 的含义是逐个取出元素，不是按下标循环。
- `total += number` 等价于 `total = total + number`。
- 初学时先少用 `while`，避免写出停不下来的循环。
- 循环里如果逻辑变复杂，优先抽成函数。

## 基础语法示例：函数

适合阶段：刚开始学 Python。

目标：把重复逻辑封装成可复用函数。

```python
def format_user(name: str, age: int) -> str:
    return f"{name} ({age})"


user_text = format_user("Sean", 28)
print(user_text)
```

需要关注：

- 函数名应该表达“做什么”，例如 `format_user` 比 `handle` 更明确。
- `return` 是函数结果；只 `print` 不 `return` 的函数很难复用和测试。
- `name: str` 和 `-> str` 是类型标注，帮助读代码和做静态检查，不会自动做运行时校验。
- 函数不要一开始就写太大；一个函数最好只完成一个明确动作。

## 基础语法示例：列表和字典

适合阶段：刚开始学 Python。

目标：掌握最常用的两个数据结构：列表表示一组同类元素，字典表示键值映射。

```python
users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "editor"},
    {"name": "Cindy", "role": "admin"},
]

admins = []
for user in users:
    if user["role"] == "admin":
        admins.append(user["name"])

print(admins)
```

需要关注：

- `list` 适合保存有顺序的一组元素。
- `dict` 适合按字段名取值，例如 `user["name"]`。
- 直接用 `user["role"]` 时，如果字段不存在会报错；不确定字段是否存在时用 `user.get("role")`。
- 这类“过滤列表”的逻辑很常见，后续可以学习 list comprehension，但入门阶段先写清楚循环。

## 基础语法示例：字符串处理

适合阶段：入门。

目标：处理用户输入、日志、文件名时，字符串方法会很常用。

```python
raw = "  python, testing, backend  "

items = []
for item in raw.strip().split(","):
    items.append(item.strip())

print(items)
```

需要关注：

- `strip()` 去掉首尾空白，不会处理字符串中间的空格。
- `split(",")` 按逗号切分字符串，结果是列表。
- 字符串是不可变对象，`strip()` 会返回新字符串，不会修改原字符串。
- 文本处理要注意大小写、空值、分隔符和编码问题。

## 基础语法示例：异常处理

适合阶段：入门到中级。

目标：知道程序失败时如何给出可控处理，而不是直接崩掉。

```python
def parse_age(text: str) -> int | None:
    try:
        age = int(text)
    except ValueError:
        return None

    if age < 0:
        return None
    return age


print(parse_age("28"))
print(parse_age("abc"))
```

需要关注：

- 只捕获你预期的异常，例如这里捕获 `ValueError`，不要随手写裸 `except`。
- 异常处理不是吞掉错误；真实程序里通常要记录日志或返回明确错误信息。
- 输入来自用户、文件、网络时，都要假设它可能不合法。
- 边界值也要处理，例如负数、空字符串、特别大的数字。

## 基础语法示例：模块导入

适合阶段：入门。

目标：理解 Python 程序通常由多个模块组成，不必把所有代码写在一个文件里。

```python
from datetime import datetime
from pathlib import Path


today = datetime.now().strftime("%Y-%m-%d")
output = Path("logs") / f"{today}.txt"

print(output)
```

需要关注：

- 优先使用标准库解决常见问题，例如时间、路径、JSON、CSV。
- `from pathlib import Path` 是导入某个具体对象；`import pathlib` 是导入整个模块。
- 文件名不要和标准库模块重名，例如不要把自己的文件命名为 `datetime.py`。
- 模块拆分的目标是让代码更好找、更好测，而不是为了拆而拆。

## 示例 1：批量重命名文件

适合阶段：入门。

目标：把一个目录下的 `.txt` 文件统一改成 `note-001.txt`、`note-002.txt` 这种格式。

```python
from pathlib import Path


def rename_notes(folder: str) -> None:
    files = sorted(Path(folder).glob("*.txt"))
    for index, path in enumerate(files, start=1):
        new_name = path.with_name(f"note-{index:03d}{path.suffix}")
        path.rename(new_name)


if __name__ == "__main__":
    rename_notes("./notes")
```

需要关注：

- 先用 `print(path, "->", new_name)` 预览结果，再真正执行 `rename`。
- 注意文件重名覆盖风险；真实脚本里要检查 `new_name.exists()`。
- 用 `pathlib` 处理路径，少拼字符串。
- 练习目标不是记住 API，而是建立“先列出、再验证、最后执行”的脚本习惯。

## 示例 2：CSV 清洗和汇总

适合阶段：入门到中级。

目标：读取订单 CSV，过滤无效数据，统计每天收入。

```python
import csv
from collections import defaultdict
from decimal import Decimal


def daily_revenue(csv_path: str) -> dict[str, Decimal]:
    revenue = defaultdict(Decimal)
    with open(csv_path, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["status"] != "paid":
                continue
            day = row["created_at"][:10]
            revenue[day] += Decimal(row["amount"])
    return dict(revenue)


if __name__ == "__main__":
    for day, amount in sorted(daily_revenue("orders.csv").items()):
        print(day, amount)
```

需要关注：

- 金额不要直接用 `float`，优先用 `Decimal`。
- 输入数据可能缺列、空值、非法金额；后续要补异常处理和错误行记录。
- 聚合逻辑要和 IO 分开，便于测试。
- CSV 小数据可以用标准库；数据清洗复杂后再引入 pandas。

## 示例 3：命令行工具

适合阶段：初级到中级。

目标：把脚本变成可以传参数的 CLI，而不是每次改代码。

```python
import argparse
from pathlib import Path


def count_lines(folder: Path, suffix: str) -> int:
    total = 0
    for path in folder.rglob(f"*{suffix}"):
        if path.is_file():
            total += len(path.read_text(encoding="utf-8").splitlines())
    return total


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder")
    parser.add_argument("--suffix", default=".py")
    args = parser.parse_args()

    total = count_lines(Path(args.folder), args.suffix)
    print(total)


if __name__ == "__main__":
    main()
```

需要关注：

- `main()` 只负责参数解析和输出，核心逻辑放到独立函数。
- 参数要有默认值、帮助信息和错误提示。
- 后续可以补 `pyproject.toml`，把它安装成真正的命令。
- 统计代码行只是练手，真正重要的是 CLI 的结构。

## 示例 4：给核心逻辑加测试

适合阶段：工程化。

目标：给纯函数补 pytest，先测业务逻辑，不急着测命令行入口。

```python
from decimal import Decimal

from revenue import daily_revenue


def test_daily_revenue(tmp_path):
    csv_file = tmp_path / "orders.csv"
    csv_file.write_text(
        "created_at,status,amount\n"
        "2026-05-01 10:00:00,paid,12.50\n"
        "2026-05-01 11:00:00,canceled,99.00\n"
        "2026-05-02 09:00:00,paid,7.25\n",
        encoding="utf-8",
    )

    assert daily_revenue(str(csv_file)) == {
        "2026-05-01": Decimal("12.50"),
        "2026-05-02": Decimal("7.25"),
    }
```

需要关注：

- 优先测试稳定的业务函数，而不是测试 `print` 输出。
- 用 `tmp_path` 创建临时文件，避免污染项目目录。
- 每个测试覆盖一个明确行为：正常路径、空文件、非法金额、缺失字段。
- 如果一个函数很难测试，通常说明 IO、时间、网络或全局状态混在核心逻辑里了。

## 示例 5：FastAPI CRUD 小服务

适合阶段：Web 后端方向。

目标：写一个最小 API，理解路由、请求体、响应模型和状态码。

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


class TodoIn(BaseModel):
    title: str
    done: bool = False


app = FastAPI()
todos: dict[int, TodoIn] = {}
next_id = 1


@app.post("/todos")
def create_todo(todo: TodoIn) -> dict:
    global next_id
    todo_id = next_id
    next_id += 1
    todos[todo_id] = todo
    return {"id": todo_id, **todo.model_dump()}


@app.get("/todos/{todo_id}")
def get_todo(todo_id: int) -> dict:
    todo = todos.get(todo_id)
    if todo is None:
        raise HTTPException(status_code=404, detail="todo not found")
    return {"id": todo_id, **todo.model_dump()}
```

需要关注：

- 这个示例只适合理解 API 形态，真实服务不能用内存字典保存数据。
- 后续要引入数据库、迁移、分页、认证、日志和测试。
- 请求模型、响应模型、错误结构要尽早规范。
- 学 Web 不只是学框架 API，还要补 HTTP、数据库、部署和可观测性。

## 示例 6：asyncio 并发请求

适合阶段：进阶语言能力。

目标：理解异步 IO 适合等待网络/文件等慢操作，不适合直接加速 CPU 密集计算。

```python
import asyncio
import time


async def fetch_mock(name: str, delay: float) -> str:
    await asyncio.sleep(delay)
    return f"{name}: done"


async def main() -> None:
    started = time.perf_counter()
    results = await asyncio.gather(
        fetch_mock("a", 1.0),
        fetch_mock("b", 1.0),
        fetch_mock("c", 1.0),
    )
    print(results)
    print(f"elapsed: {time.perf_counter() - started:.2f}s")


asyncio.run(main())
```

需要关注：

- `async` 函数里遇到阻塞调用会拖慢整个事件循环。
- 并发不是越多越好，真实网络请求要加超时、重试、限流和错误收集。
- CPU 密集任务优先考虑进程池、原生扩展或改算法。
- 异步代码会增加复杂度；只有任务确实在等待 IO 时收益才明显。

## 示例 7：pandas 分组统计

适合阶段：数据处理方向。

目标：用 pandas 做表格清洗和聚合。

```python
import pandas as pd


orders = pd.read_csv("orders.csv")
orders["created_at"] = pd.to_datetime(orders["created_at"])
orders["amount"] = pd.to_numeric(orders["amount"], errors="coerce")

paid = orders[orders["status"] == "paid"].dropna(subset=["amount"])
paid["day"] = paid["created_at"].dt.date

summary = paid.groupby("day", as_index=False)["amount"].sum()
summary.to_csv("daily_revenue.csv", index=False)
```

需要关注：

- 先检查数据形状：列名、行数、缺失值、重复值、类型。
- `errors="coerce"` 会把非法金额变成空值，后续要统计有多少脏数据被丢弃。
- pandas 很适合探索和批处理，但长期任务要保留输入输出样例和测试数据。
- 结果导出前要确认排序、时区、金额精度和字段命名。

# 阶段检查清单

## 入门合格

- 能独立安装 Python、创建虚拟环境、运行脚本。
- 能熟练使用列表、字典、字符串和文件读写。
- 能读懂异常堆栈并定位到出错行。
- 能写一个解决真实小问题的脚本。

## 中级合格

- 能把脚本拆成模块，写清楚入口和 README。
- 能使用标准库完成常见任务，而不是动不动引入依赖。
- 能给关键逻辑补 pytest 测试。
- 能管理依赖和虚拟环境。
- 能解释同步、线程、进程、异步 IO 的基本差异。

## 进阶合格

- 能设计较清晰的模块边界和错误处理策略。
- 能用类型标注降低维护成本。
- 能读懂框架中的装饰器、上下文管理器、异步函数和 ORM 模型。
- 能围绕一个方向做完整项目，例如 API 服务、数据处理流水线、自动化工具或内部 CLI。

# 推荐学习顺序

1. 官方教程过一遍，不追求记住所有细节。
2. 用 Automate the Boring Stuff 做 2-3 个实用小脚本。
3. 选一个小项目，补 `argparse`、`logging`、README 和虚拟环境。
4. 学 pytest，把小项目核心逻辑测起来。
5. 学 packaging 和类型标注，把项目做得更像可维护工程。
6. 选择 Web 后端、数据处理、自动化或 AI 工程其中一个方向深入。
7. 遇到语言机制问题，再回查官方 reference 和标准库文档。

# 资源速查

| 资源 | 适合阶段 | 用法 |
| --- | --- | --- |
| [Python 官方教程（中文）](https://docs.python.org/zh-cn/3/tutorial/) | 入门 | 按章节建立主线。 |
| [Python 官方教程（英文）](https://docs.python.org/3/tutorial/) | 入门/查证 | 对照中文，确认术语和原始表述。 |
| [Python Standard Library](https://docs.python.org/3/library/) | 初级到进阶 | 查标准库 API，优先级高于博客。 |
| [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/) | 中级 | 学项目打包、安装和发布基础。 |
| [pytest documentation](https://docs.pytest.org/en/stable/) | 中级 | 学测试组织、fixture 和断言。 |
| [mypy Getting Started](https://mypy.readthedocs.io/en/stable/getting_started.html) | 中级/进阶 | 建立类型检查习惯。 |
| [Automate the Boring Stuff](https://automatetheboringstuff.com/) | 入门实战 | 用脚本解决日常自动化问题。 |
| [Real Python](https://realpython.com/) | 查漏补缺 | 查专题文章，注意部分内容可能付费。 |
| [FastAPI](https://fastapi.tiangolo.com/) | Web 后端 | 做 API 服务和现代 Python 后端。 |
| [Django Tutorial](https://docs.djangoproject.com/en/stable/intro/tutorial01/) | Web 后端 | 学完整 Web 框架和应用结构。 |
| [pandas Intro Tutorials](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) | 数据处理 | 学表格数据处理。 |

# 关联页面

- [技术学习资料](技术学习资料.md)
- [后端知识体系](后端知识体系.md)
