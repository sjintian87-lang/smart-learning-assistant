"""
智学编程 - 智能学习助手 Web版
使用Streamlit构建的网页应用
"""

import streamlit as st
import sys
import random
from datetime import datetime
import json

# 页面配置
st.set_page_config(
    page_title="智学编程 - 智能学习助手",
    page_icon="📚",
    layout="wide"
)

# ============== 知识库 ==============
KNOWLEDGE_BASE = {
    "数据结构": {
        "数组": {
            "difficulty": 1,
            "concepts": ["索引访问", "遍历", "插入删除"],
            "examples": ["实现数组的反转", "找出数组中的最大值和最小值", "实现数组的去重"],
            "code": '''# 数组的基本操作
arr = [1, 2, 3, 4, 5]

# 索引访问
print(f"第一个元素: {arr[0]}")
print(f"最后一个元素: {arr[-1]}")

# 遍历
print("遍历数组:")
for i, val in enumerate(arr):
    print(f"  索引{i}: {val}")

# 反转数组
reversed_arr = arr[::-1]
print(f"反转后: {reversed_arr}")'''
        },
        "链表": {
            "difficulty": 2,
            "concepts": ["节点结构", "指针操作", "链表遍历"],
            "examples": ["实现单链表的插入和删除", "反转一个单链表", "检测链表是否有环"],
            "code": '''# 单链表的实现
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 创建链表: 1 -> 2 -> 3
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

# 遍历链表
current = head
print("链表内容:")
while current:
    print(f"  节点值: {current.val}")
    current = current.next'''
        },
        "栈和队列": {
            "difficulty": 2,
            "concepts": ["后进先出", "先进先出", "应用场景"],
            "examples": ["用数组实现一个栈", "判断括号字符串是否有效", "用队列实现栈"],
            "code": '''# 用列表实现栈
stack = []

# 入栈
stack.append(1)
stack.append(2)
stack.append(3)
print(f"栈内容: {stack}")

# 出栈
top = stack.pop()
print(f"出栈元素: {top}")
print(f"栈顶元素: {stack[-1]}")'''
        },
        "树": {
            "difficulty": 3,
            "concepts": ["二叉树结构", "遍历方式", "递归思想"],
            "examples": ["实现二叉树的前中后序遍历", "计算二叉树的最大深度", "判断是否为平衡二叉树"],
            "code": '''# 二叉树的实现和遍历
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 创建二叉树
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# 前序遍历
def preorder(node):
    if node:
        print(f"访问节点: {node.val}")
        preorder(node.left)
        preorder(node.right)

print("前序遍历:")
preorder(root)'''
        }
    },
    "算法": {
        "排序算法": {
            "difficulty": 2,
            "concepts": ["比较排序", "时间复杂度", "稳定性"],
            "examples": ["实现冒泡排序", "实现快速排序", "实现归并排序"],
            "code": '''# 冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print(f"原始数组: {arr}")
print(f"排序结果: {bubble_sort(arr.copy())}")'''
        },
        "搜索算法": {
            "difficulty": 2,
            "concepts": ["二分查找", "线性搜索", "搜索策略"],
            "examples": ["实现二分查找", "在旋转数组中查找目标值", "查找第一个等于目标值的元素"],
            "code": '''# 二分查找
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1, 3, 5, 7, 9, 11, 13, 15]
result = binary_search(arr, 7)
print(f"在 {arr} 中查找 7，索引为: {result}")'''
        },
        "动态规划": {
            "difficulty": 4,
            "concepts": ["状态定义", "状态转移", "边界条件"],
            "examples": ["计算斐波那契数列", "爬楼梯问题", "最长递增子序列"],
            "code": '''# 斐波那契数列（动态规划）
def fib_dp(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[0], dp[1] = 0, 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

n = 10
print(f"斐波那契数列第{n}项: {fib_dp(n)}")'''
        }
    },
    "编程基础": {
        "变量与类型": {
            "difficulty": 1,
            "concepts": ["数据类型", "变量声明", "类型转换"],
            "examples": ["判断变量的类型", "实现不同类型之间的转换", "处理用户输入的类型问题"],
            "code": '''# 变量与类型
x = 10
y = 3.14
z = "Hello"
flag = True

print(f"x的类型: {type(x)}")
print(f"y的类型: {type(y)}")
print(f"z的类型: {type(z)}")
print(f"flag的类型: {type(flag)}")

# 类型转换
num_str = "123"
num_int = int(num_str)
print(f"字符串转整数: {num_int + 10}")'''
        },
        "控制流": {
            "difficulty": 1,
            "concepts": ["条件判断", "循环结构", "流程控制"],
            "examples": ["实现成绩等级判断", "打印九九乘法表", "实现猜数字游戏"],
            "code": '''# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\\t")
    print()

# 成绩等级判断
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print(f"成绩 {score} 分，等级: {grade}")'''
        },
        "函数": {
            "difficulty": 2,
            "concepts": ["函数定义", "参数传递", "返回值"],
            "examples": ["实现一个计算器函数", "用递归实现阶乘", "实现函数作为参数传递"],
            "code": '''# 递归实现阶乘
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# 函数作为参数
def apply_twice(func, x):
    return func(func(x))

print(f"5! = {factorial(5)}")
print(f"apply_twice(lambda x: x+3, 5) = {apply_twice(lambda x: x+3, 5)}")'''
        }
    }
}

# 练习题库
PRACTICE_QUESTIONS = {
    "数组": [
        {
            "title": "数组反转",
            "description": "实现一个函数，将数组原地反转",
            "input_example": "[1, 2, 3, 4, 5]",
            "output_example": "[5, 4, 3, 2, 1]",
            "hints": ["考虑使用双指针", "注意边界条件"]
        },
        {
            "title": "两数之和",
            "description": "在数组中找出两个数，使它们的和等于目标值，返回索引",
            "input_example": "nums=[2,7,11,15], target=9",
            "output_example": "[0, 1]",
            "hints": ["考虑哈希表优化", "注意去重"]
        }
    ],
    "链表": [
        {
            "title": "链表反转",
            "description": "反转一个单链表",
            "input_example": "1->2->3->4->5",
            "output_example": "5->4->3->2->1",
            "hints": ["画图理解指针变化", "保存next节点"]
        }
    ],
    "栈和队列": [
        {
            "title": "有效的括号",
            "description": "判断括号字符串是否有效",
            "input_example": "()[]{}",
            "output_example": "True",
            "hints": ["使用栈结构", "处理各种情况"]
        }
    ],
    "树": [
        {
            "title": "二叉树遍历",
            "description": "实现二叉树的前序遍历",
            "input_example": "树结构",
            "output_example": "根-左-右",
            "hints": ["递归或迭代", "理解遍历顺序"]
        }
    ],
    "排序算法": [
        {
            "title": "冒泡排序",
            "description": "实现冒泡排序算法",
            "input_example": "[64, 34, 25, 12]",
            "output_example": "[12, 25, 34, 64]",
            "hints": ["比较相邻元素", "外层循环控制轮数"]
        }
    ],
    "搜索算法": [
        {
            "title": "二分查找",
            "description": "在有序数组中查找目标值",
            "input_example": "[1,3,5,7,9], target=7",
            "output_example": "3",
            "hints": ["利用有序特性", "注意边界条件"]
        }
    ],
    "动态规划": [
        {
            "title": "爬楼梯",
            "description": "每次爬1或2级，求到n级的方法数",
            "input_example": "n=5",
            "output_example": "8",
            "hints": ["dp[i]表示方法数", "状态转移方程"]
        }
    ]
}

# ============== 会话状态初始化 ==============
def init_session_state():
    if 'mastery_level' not in st.session_state:
        st.session_state.mastery_level = {}
    if 'practice_records' not in st.session_state:
        st.session_state.practice_records = []
    if 'current_topic' not in st.session_state:
        st.session_state.current_topic = None
    if 'practice_result' not in st.session_state:
        st.session_state.practice_result = None

init_session_state()

# ============== 页面样式 ==============
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        color: #1e88e5;
        padding: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .feature-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        margin: 0.5rem 0;
    }
    .code-block {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 5px;
        font-family: 'Courier New', monospace;
        font-size: 0.9rem;
    }
    .stat-card {
        background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        padding: 1rem;
        border-radius: 8px;
        color: white;
        text-align: center;
    }
    .warning-text {
        color: #ff6b6b;
        font-weight: bold;
    }
    .success-text {
        color: #51cf66;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ============== 主页面 ==============
st.markdown('<p class="main-header">📚 智学编程 - 智能学习助手</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">针对实践型学习风格设计 | 数据结构与算法学习平台</p>', unsafe_allow_html=True)

# 侧边栏导航
with st.sidebar:
    st.markdown("## 🎯 学习导航")
    page = st.radio(
        "选择功能",
        ["📖 个性化讲解", "💻 练习中心", "📊 知识图谱", "🔍 学习诊断", "📅 学习计划"],
        index=0
    )

    st.markdown("---")

    # 学习统计
    st.markdown("### 📈 学习统计")
    total_practice = len(st.session_state.practice_records)
    mastered_count = sum(1 for v in st.session_state.mastery_level.values() if v >= 0.8)

    col1, col2 = st.columns(2)
    with col1:
        st.metric("练习次数", total_practice)
    with col2:
        st.metric("已精通", mastered_count)

    # 学习风格提示
    st.markdown("---")
    st.info("👤 您的学习风格：**实践型**\n\n建议：先看代码 → 动手练习 → 查看反馈")

# ============== 个性化讲解页面 ==============
if page == "📖 个性化讲解":
    st.markdown("## 📖 个性化讲解")
    st.markdown("*针对实践型学习者，采用「代码先行」的讲解策略*")

    # 选择类别和主题
    col1, col2 = st.columns(2)
    with col1:
        category = st.selectbox("选择类别", list(KNOWLEDGE_BASE.keys()))
    with col2:
        topic = st.selectbox("选择主题", list(KNOWLEDGE_BASE[category].keys()))

    if category and topic:
        topic_info = KNOWLEDGE_BASE[category][topic]

        # 显示掌握度
        mastery = st.session_state.mastery_level.get(topic, 0)
        st.progress(mastery, text=f"掌握度: {mastery*100:.1f}%")

        # 代码示例
        st.markdown("### 💻 代码示例")
        st.markdown('<div class="code-block">```python\n' + topic_info["code"] + '\n```</div>', unsafe_allow_html=True)

        # 核心概念
        st.markdown("### 📝 核心概念")
        for i, concept in enumerate(topic_info["concepts"], 1):
            st.markdown(f"- **{concept}**")

        # 实践建议
        st.markdown("### ✍️ 动手实践")
        for example in topic_info["examples"]:
            st.markdown(f"- {example}")

        # 难度标识
        stars = "⭐" * topic_info["difficulty"] + "☆" * (5 - topic_info["difficulty"])
        st.markdown(f"**难度等级**: {stars}")

        # 开始练习按钮
        if st.button(f"🚀 开始练习 {topic}", type="primary", use_container_width=True):
            st.session_state.current_topic = topic
            st.rerun()

# ============== 练习中心页面 ==============
elif page == "💻 练习中心":
    st.markdown("## 💻 练习中心")
    st.markdown("*选择主题开始练习，系统会自动调整难度*")

    # 选择练习主题
    all_topics = []
    for cat, topics in KNOWLEDGE_BASE.items():
        for topic in topics.keys():
            all_topics.append(topic)

    selected_topic = st.selectbox("选择练习主题", all_topics)

    # 根据掌握度推荐难度
    mastery = st.session_state.mastery_level.get(selected_topic, 0)
    if mastery < 0.3:
        recommended_diff = "基础"
    elif mastery < 0.7:
        recommended_diff = "中等"
    else:
        recommended_diff = "进阶"

    st.info(f"📊 推荐难度: {recommended_diff} (当前掌握度: {mastery*100:.1f}%)")

    # 生成练习题
    if st.button("🎲 生成练习题", type="primary", use_container_width=True):
        questions = PRACTICE_QUESTIONS.get(selected_topic, PRACTICE_QUESTIONS["数组"])
        question = random.choice(questions)

        st.session_state.current_question = question
        st.session_state.practice_topic = selected_topic

    # 显示当前题目
    if hasattr(st.session_state, 'current_question') and st.session_state.current_question:
        question = st.session_state.current_question
        topic = st.session_state.practice_topic

        st.markdown("---")
        st.markdown(f"### 📝 {question['title']}")
        st.markdown(f"**题目描述**: {question['description']}")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**输入示例**")
            st.code(question["input_example"], language=None)
        with col2:
            st.markdown("**输出示例**")
            st.code(question["output_example"], language=None)

        # 提示
        with st.expander("💡 查看提示"):
            for hint in question["hints"]:
                st.markdown(f"- {hint}")

        # 代码输入区
        st.markdown("### 📝 请在这里编写代码")
        user_code = st.text_area(
            "编写你的解答代码",
            height=200,
            placeholder="# 在这里编写代码\n..."
        )

        # 提交答案
        col1, col2 = st.columns(2)
        with col1:
            submit = st.button("✅ 提交答案", type="primary", use_container_width=True)
        with col2:
            hint = st.button("❓ 再给一个提示", use_container_width=True)

        if submit:
            # 模拟评分
            score = random.randint(60, 100)
            passed_tests = max(1, int(score / 33))

            # 记录练习
            record = {
                "topic": topic,
                "score": score,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
            st.session_state.practice_records.append(record)

            # 更新掌握度
            old_mastery = st.session_state.mastery_level.get(topic, 0)
            st.session_state.mastery_level[topic] = 0.7 * old_mastery + 0.3 * (score / 100)

            # 显示结果
            st.session_state.practice_result = {
                "score": score,
                "passed": passed_tests,
                "total": 3
            }

        # 显示结果
        if st.session_state.practice_result:
            result = st.session_state.practice_result
            st.markdown("---")

            if result["score"] >= 90:
                st.success(f"🎉 太棒了！得分: {result['score']}分 ({result['passed']}/{result['total']} 测试通过)")
                st.balloons()
            elif result["score"] >= 60:
                st.warning(f"👍 不错！得分: {result['score']}分 ({result['passed']}/{result['total']} 测试通过)")
                st.info("💡 建议：继续挑战更高难度！")
            else:
                st.error(f"💪 加油！得分: {result['score']}分 ({result['passed']}/{result['total']} 测试通过)")
                st.info("💡 建议：重新查看讲解，理解基础概念后再试一次！")

            # 清除结果
            st.session_state.practice_result = None

# ============== 知识图谱页面 ==============
elif page == "📊 知识图谱":
    st.markdown("## 📊 知识掌握度图谱")
    st.markdown("*可视化展示各知识点的学习进度*")

    # 绘制每个类别的掌握度
    for category, topics in KNOWLEDGE_BASE.items():
        st.markdown(f"### 【{category}】")

        cols = st.columns(2)
        for idx, (topic, info) in enumerate(topics.items()):
            mastery = st.session_state.mastery_level.get(topic, 0)

            with cols[idx % 2]:
                st.markdown(f"**{topic}**")
                st.progress(mastery, text=f"{mastery*100:.1f}%")

                if mastery >= 0.8:
                    st.markdown("⭐⭐⭐ 精通")
                elif mastery >= 0.6:
                    st.markdown("⭐⭐ 良好")
                elif mastery >= 0.4:
                    st.markdown("⭐ 入门")
                else:
                    st.markdown("📚 待学习")

                st.markdown("---")

    # 推荐学习
    st.markdown("### 🎯 推荐学习路径")

    # 找出掌握度最低的主题
    sorted_topics = sorted(st.session_state.mastery_level.items(), key=lambda x: x[1])
    if sorted_topics:
        weakest = sorted_topics[0]
        st.warning(f"建议优先学习 **{weakest[0]}** (当前掌握度: {weakest[1]*100:.1f}%)")
    else:
        st.info("开始学习吧！建议从【数组】开始")

# ============== 学习诊断页面 ==============
elif page == "🔍 学习诊断":
    st.markdown("## 🔍 学习诊断报告")
    st.markdown("*基于你的练习记录，分析薄弱点和优势*")

    if len(st.session_state.practice_records) == 0:
        st.info("📝 开始一些练习后，这里会显示你的学习诊断报告")

    else:
        # 统计各主题表现
        topic_stats = {}
        for record in st.session_state.practice_records:
            topic = record["topic"]
            if topic not in topic_stats:
                topic_stats[topic] = {"scores": [], "count": 0}
            topic_stats[topic]["scores"].append(record["score"])
            topic_stats[topic]["count"] += 1

        # 薄弱点
        st.markdown("### ⚠️ 薄弱点")
        weaknesses = [(t, s) for t, s in topic_stats.items() if sum(s["scores"])/len(s["scores"]) < 60]

        if weaknesses:
            for topic, stats in sorted(weaknesses, key=lambda x: sum(x[1]["scores"])/len(x[1]["scores"])):
                avg = sum(stats["scores"]) / len(stats["scores"])
                st.error(f"- **{topic}**: 平均分 {avg:.1f}分 (练习{stats['count']}次)")
        else:
            st.success("✅ 没有薄弱点！继续保持！")

        # 优势项
        st.markdown("### ✅ 优势项")
        strengths = [(t, s) for t, s in topic_stats.items() if sum(s["scores"])/len(s["scores"]) >= 80]

        if strengths:
            for topic, stats in sorted(strengths, key=lambda x: sum(x[1]["scores"])/len(x[1]["scores"]), reverse=True):
                avg = sum(stats["scores"]) / len(stats["scores"])
                st.success(f"- **{topic}**: 平均分 {avg:.1f}分 (练习{stats['count']}次)")
        else:
            st.info("💪 继续加油，提升薄弱项！")

        # 学习建议
        st.markdown("### 💡 学习建议")
        if weaknesses:
            st.markdown("- 建议先巩固薄弱知识点，再学习新内容")
            st.markdown("- 对于平均分低于60的主题，建议重新查看讲解")
            st.markdown("- 多做基础题，理解核心概念后再挑战难题")
        else:
            st.markdown("- 继续保持当前学习节奏")
            st.markdown("- 可以尝试更高难度的挑战")

# ============== 学习计划页面 ==============
elif page == "📅 学习计划":
    st.markdown("## 📅 学习计划")
    st.markdown("*根据你的掌握情况，智能生成学习计划*")

    plan_days = st.slider("计划天数", 3, 14, 7)

    # 收集所有主题及其掌握度
    topics_priority = []
    for cat, topics in KNOWLEDGE_BASE.items():
        for topic, info in topics.items():
            mastery = st.session_state.mastery_level.get(topic, 0)
            topics_priority.append({
                "topic": topic,
                "mastery": mastery,
                "difficulty": info["difficulty"]
            })

    # 按掌握度排序
    topics_priority.sort(key=lambda x: (x["mastery"], x["difficulty"]))

    # 生成计划
    for day in range(1, plan_days + 1):
        if day <= len(topics_priority):
            plan = topics_priority[day - 1]
            topic = plan["topic"]
            mastery = plan["mastery"]

            with st.expander(f"📅 第{day}天 - {topic} (掌握度: {mastery*100:.1f}%)", expanded=(day<=3)):
                st.markdown("**建议任务:**")
                st.checkbox("查看个性化讲解", value=True)
                st.checkbox("完成2-3道练习题", value=False)
                st.checkbox("分析错题原因", value=False)
                st.checkbox("复习巩固今天内容", value=False)

                st.markdown("**学习步骤:**")
                st.markdown("1. 先看代码示例，运行观察结果")
                st.markdown("2. 理解核心概念")
                st.markdown("3. 完成练习题")
                st.markdown("4. 查看反馈，分析错题")
        else:
            with st.expander(f"📅 第{day}天 - 复习巩固", expanded=False):
                st.markdown("**建议任务:**")
                st.checkbox("复习本周学习内容", value=True)
                st.checkbox("重做错题", value=False)
                st.checkbox("总结学习心得", value=False)

# 页脚
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>"
    "智学编程 v1.0 | 智能学习助手 | 针对实践型学习风格设计"
    "</p>",
    unsafe_allow_html=True
)
