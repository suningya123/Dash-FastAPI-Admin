from fastapi import APIRouter, Request
from fastapi import Depends, HTTPException, Header
from config.get_db import get_db
from service.login_service import get_current_user, get_password_hash
from service.user_service import *
from mapper.schema.user_schema import *
from mapper.crud.user_crud import *
from utils.response_tool import *
from utils.log_tool import *


userController = APIRouter()


@userController.post("/user/get", response_model=UserPageObjectResponse)
async def get_system_user_list(request: Request, user_query: UserPageObject, token: Optional[str] = Header(...), query_db: Session = Depends(get_db)):
    try:
        current_user = await get_current_user(request, token, query_db)
        if current_user == "用户token已失效，请重新登录" or current_user == "用户token不合法":
            logger.warning(current_user)
            return response_401(data="", message=current_user)
        else:
            user_query_result = get_user_list_services(query_db, user_query)
            logger.info('获取成功')
            return response_200(data=user_query_result, message="获取成功")
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@userController.post("/user/add", response_model=CrudUserResponse)
async def add_system_user(request: Request, add_user: AddUserModel, token: Optional[str] = Header(...), query_db: Session = Depends(get_db)):
    try:
        current_user = await get_current_user(request, token, query_db)
        if current_user == "用户token已失效，请重新登录" or current_user == "用户token不合法":
            logger.warning(current_user)
            return response_401(data="", message=current_user)
        else:
            add_user.password = get_password_hash(add_user.password)
            add_user.create_by = current_user.user.user_name
            add_user.update_by = current_user.user.user_name
            add_user_result = add_user_services(query_db, add_user)
            logger.info(add_user_result.message)
            if add_user_result.is_success:
                return response_200(data=add_user_result, message=add_user_result.message)
            else:
                return response_400(data="", message=add_user_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@userController.post("/user/edit", response_model=CrudUserResponse)
async def edit_system_user(request: Request, edit_user: AddUserModel, token: Optional[str] = Header(...), query_db: Session = Depends(get_db)):
    try:
        current_user = await get_current_user(request, token, query_db)
        if current_user == "用户token已失效，请重新登录" or current_user == "用户token不合法":
            logger.warning(current_user)
            return response_401(data="", message=current_user)
        else:
            edit_user.update_by = current_user.user.user_name
            edit_user.update_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            edit_user_result = edit_user_services(query_db, edit_user)
            if edit_user_result.is_success:
                logger.info(edit_user_result.message)
                return response_200(data=edit_user_result, message=edit_user_result.message)
            else:
                logger.warning(edit_user_result.message)
                return response_400(data="", message=edit_user_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@userController.post("/user/delete", response_model=CrudUserResponse)
async def delete_system_user(request: Request, delete_user: DeleteUserModel, token: Optional[str] = Header(...), query_db: Session = Depends(get_db)):
    try:
        current_user = await get_current_user(request, token, query_db)
        if current_user == "用户token已失效，请重新登录" or current_user == "用户token不合法":
            logger.warning(current_user)
            return response_401(data="", message=current_user)
        else:
            delete_user_result = delete_user_services(query_db, delete_user)
            if delete_user_result.is_success:
                logger.info(delete_user_result.message)
                return response_200(data=delete_user_result, message=delete_user_result.message)
            else:
                logger.warning(delete_user_result.message)
                return response_400(data="", message=delete_user_result.message)
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")


@userController.get("/user/{user_id}", response_model=UserDetailModel)
async def query_detail_system_user(request: Request, user_id: int, token: Optional[str] = Header(...), query_db: Session = Depends(get_db)):
    try:
        current_user = await get_current_user(request, token, query_db)
        if current_user == "用户token已失效，请重新登录" or current_user == "用户token不合法":
            logger.warning(current_user)
            return response_401(data="", message=current_user)
        else:
            delete_user_result = detail_user_services(query_db, user_id)
            logger.info(f'获取user_id为{user_id}的信息成功')
            return response_200(data=delete_user_result, message='获取成功')
    except Exception as e:
        logger.exception(e)
        return response_500(data="", message="接口异常")
