from pydantic import BaseModel
from typing import Union, Optional


class TokenData(BaseModel):
    """
    token解析结果
    """
    user_id: Union[int, None] = None


class UserModel(BaseModel):
    """
    用户表对应pydantic模型
    """
    user_id: Optional[int]
    dept_id: Optional[int]
    user_name: Optional[str]
    nick_name: Optional[str]
    user_type: Optional[str]
    email: Optional[str]
    phonenumber: Optional[str]
    sex: Optional[str]
    avatar: Optional[str]
    password: Optional[str]
    status: Optional[str]
    del_flag: Optional[str]
    login_ip: Optional[str]
    login_date: Optional[str]
    create_by: Optional[str]
    create_time: Optional[str]
    update_by: Optional[str]
    update_time: Optional[str]
    remark: Optional[str]

    class Config:
        orm_mode = True


class UserRoleModel(BaseModel):
    """
    用户和角色关联表对应pydantic模型
    """
    user_id: Optional[int]
    role_id: Optional[int]

    class Config:
        orm_mode = True


class UserPostModel(BaseModel):
    """
    用户与岗位关联表对应pydantic模型
    """
    user_id: Optional[int]
    post_id: Optional[int]

    class Config:
        orm_mode = True


class DeptModel(BaseModel):
    """
    部门表对应pydantic模型
    """
    dept_id: Optional[int]
    parent_id: Optional[int]
    ancestors: Optional[str]
    dept_name: Optional[str]
    order_num: Optional[int]
    leader: Optional[str]
    phone: Optional[str]
    email: Optional[str]
    status: Optional[str]
    del_flag: Optional[str]
    create_by: Optional[str]
    create_time: Optional[str]
    update_by: Optional[str]
    update_time: Optional[str]

    class Config:
        orm_mode = True


class RoleModel(BaseModel):
    """
    角色表对应pydantic模型
    """
    role_id: Optional[int]
    role_name: Optional[str]
    role_key: Optional[str]
    role_sort: Optional[int]
    data_scope: Optional[str]
    menu_check_strictly: Optional[int]
    dept_check_strictly: Optional[int]
    status: Optional[str]
    del_flag: Optional[str]
    create_by: Optional[str]
    create_time: Optional[str]
    update_by: Optional[str]
    update_time: Optional[str]
    remark: Optional[str]

    class Config:
        orm_mode = True


class PostModel(BaseModel):
    """
    岗位信息表对应pydantic模型
    """
    post_id: Optional[int]
    post_code: Optional[str]
    post_name: Optional[str]
    post_sort: Optional[int]
    status: Optional[str]
    create_by: Optional[str]
    create_time: Optional[str]
    update_by: Optional[str]
    update_time: Optional[str]
    remark: Optional[str]

    class Config:
        orm_mode = True


class CurrentUserInfo(BaseModel):
    """
    数据库返回当前用户信息
    """
    user_basic_info: list[UserModel]
    user_dept_info: list[DeptModel]
    user_role_info: list[RoleModel]
    user_post_info: list[PostModel]
    user_menu_info: list


class UserDetailModel(BaseModel):
    """
    获取用户详情信息响应模型
    """
    user: UserModel
    dept: DeptModel
    role: list[RoleModel]
    post: list[PostModel]


class CurrentUserInfoServiceResponse(UserDetailModel):
    """
    获取当前用户信息响应模型
    """
    menu: list


class UserPageObject(UserModel):
    """
    用户管理分页查询模型
    """
    create_time_start: Optional[str]
    create_time_end: Optional[str]
    page_num: int
    page_size: int


class UserInfoJoinDept(BaseModel):
    """
    数据库查询用户列表返回模型
    """
    user_id: Optional[int]
    dept_id: Optional[int]
    dept_name: Optional[str]
    user_name: Optional[str]
    nick_name: Optional[str]
    user_type: Optional[str]
    email: Optional[str]
    phonenumber: Optional[str]
    sex: Optional[str]
    avatar: Optional[str]
    status: Optional[str]
    del_flag: Optional[str]
    login_ip: Optional[str]
    login_date: Optional[str]
    create_by: Optional[str]
    create_time: Optional[str]
    update_by: Optional[str]
    update_time: Optional[str]
    remark: Optional[str]


class UserPageObjectResponse(BaseModel):
    """
    用户管理列表分页查询返回模型
    """
    rows: list[UserInfoJoinDept] = []
    page_num: int
    page_size: int
    total: int
    has_next: bool


class AddUserModel(UserModel):
    """
    新增用户模型
    """
    role_id: Optional[str]
    post_id: Optional[str]


class DeleteUserModel(BaseModel):
    """
    删除用户模型
    """
    user_ids: str
    update_by: Optional[str]
    update_time: Optional[str]


class CrudUserResponse(BaseModel):
    """
    操作用户响应模型
    """
    is_success: bool
    message: str


class DeptInfo(BaseModel):
    """
    查询部门树
    """
    dept_id: int
    dept_name: str
    ancestors: str


class RoleInfo(BaseModel):
    """
    用户角色信息
    """
    role_info: list


class MenuList(BaseModel):
    """
    用户菜单信息
    """
    menu_info: list