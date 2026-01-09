# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : assert_utils.py
# @author   : 李然 
# @Time     :  09:32
# @Copyright: 焕新生活
import pytest
from typing import Union, List, Dict, Any

class AssertUtils:
    """pytest 通用断言工具类"""

    @staticmethod
    def assert_status_code(
        actual_code: int,
        expected_code: int = 200,
        case_desc: str = "接口请求状态码"
    ) -> None:
        """
        校验状态码（接口自动化专用）
        :param actual_code: 实际响应状态码
        :param expected_code: 预期状态码，默认200
        :param case_desc: 用例描述，用于定位失败场景
        """
        assert actual_code == expected_code, \
            f"【{case_desc}】状态码校验失败\n预期：{expected_code}\n实际：{actual_code}"

    @staticmethod
    def _get_field_value(data: Any, field_path: str) -> Any:
        """
        递归获取嵌套字段的值（内部工具方法）
        支持的字段路径格式：
        - 单层："token"
        - 多层："data.user.id"
        - 列表索引："data.list[0].name"
        """
        # 分割字段路径（处理列表索引，比如 "list[0]" → ["list", "0"]）
        import re
        parts = re.split(r'\.|\[|\]', field_path)
        # 过滤空字符串（比如 "list[0]" 分割后会有空值）
        parts = [p for p in parts if p.strip()]

        current = data
        try:
            for part in parts:
                if current is None:
                    raise KeyError(f"字段路径中断，当前值为None，无法获取后续字段：{part}")
                # 如果是字典，直接通过key取值
                if isinstance(current, dict):
                    current = current[part]
                # 如果是列表，通过索引取值（索引必须是数字）
                elif isinstance(current, list):
                    idx = int(part)
                    if idx >= len(current):
                        raise IndexError(f"列表索引越界：{part}，列表长度：{len(current)}")
                    current = current[idx]
                # 既不是字典也不是列表，无法继续取值
                else:
                    raise TypeError(f"无法从类型 {type(current)} 中获取字段：{part}")
            return current
        except (KeyError, IndexError, TypeError) as e:
            # 捕获异常，返回特殊标记
            return f"__FIELD_NOT_FOUND__: {str(e)}"

    @staticmethod
    def assert_response_field(
            resp_json: Dict[str, Any],
            required_fields: List[str],
            case_desc: str = "接口响应"
            ) -> None:
        """
        增强版：校验响应体必选字段是否存在（支持多层嵌套、列表索引）
        :param resp_json: 接口响应字典
        :param required_fields: 必选字段路径列表，支持格式：
                                ["token", "data.user.id", "data.list[0].name"]
        :param case_desc: 用例描述
        """
        missing_fields = []
        for field in required_fields:
            field_value = AssertUtils._get_field_value(resp_json, field)
            # 如果返回特殊标记，说明字段不存在或路径错误
            if isinstance(field_value, str) and field_value.startswith("__FIELD_NOT_FOUND__"):
                missing_fields.append(f"{field} → {field_value.split(':')[1].strip()}")

        # 断言：没有缺失字段
        assert len(missing_fields) == 0, \
            f"【{case_desc}】响应体缺失必选字段或字段路径错误\n" \
            f"缺失/错误字段：\n  {chr(10).join(missing_fields)}\n" \
            f"响应体：{resp_json}"

    @staticmethod
    def assert_business_code(
        actual_code: Union[int, str],
        expected_code: Union[int, str] = 0,
        case_desc: str = "业务逻辑"
    ) -> None:
        """
        校验业务码（接口自动化专用，如 code:0 代表成功）
        :param actual_code: 实际业务码
        :param expected_code: 预期业务码，默认0
        :param case_desc: 用例描述
        """
        assert actual_code == expected_code, \
            f"【{case_desc}】业务码校验失败\n预期：{expected_code}\n实际：{actual_code}"

    @staticmethod
    def assert_value_equal(
        actual: Any,
        expected: Any,
        check_desc: str = "数据校验"
    ) -> None:
        """
        通用等值校验（支持所有数据类型：字符串、数字、字典、列表）
        :param actual: 实际值
        :param expected: 预期值
        :param check_desc: 校验描述
        """
        assert actual == expected, \
            f"【{check_desc}】等值校验失败\n预期：{expected}\n实际：{actual}"

    @staticmethod
    def assert_value_in(
            actual: Any,
            container: Union[List, Dict, str],
            check_desc: str = "包含校验"
    ) -> None:
        """
        通用包含校验（如元素在列表中、字段在字典中、子串在字符串中）
        :param actual: 待校验的目标值
        :param container: 容器（列表/字典/字符串）
        :param check_desc: 校验描述
        """
        assert actual in container, \
            f"【{check_desc}】包含校验失败\n目标值：{actual}\n容器：{container}"

    @staticmethod
    def assert_float_equal(
        actual: float,
        expected: float,
        rel_tol: float = 1e-9,
        check_desc: str = "浮点数校验"
    ) -> None:
        """
        浮点数等值校验（解决精度问题）
        :param actual: 实际浮点数
        :param expected: 预期浮点数
        :param rel_tol: 相对误差容忍度，默认1e-9
        :param check_desc: 校验描述
        """
        assert actual == pytest.approx(expected, rel=rel_tol), \
            f"【{check_desc}】浮点数校验失败\n预期：{expected}\n实际：{actual}\n误差容忍度：{rel_tol}"

# 实例化工具类，方便用例直接调用
assert_util = AssertUtils()