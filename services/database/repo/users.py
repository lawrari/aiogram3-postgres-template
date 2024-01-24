from typing import Union

from sqlalchemy.dialects.postgresql import insert

from services.database.models import User
from services.database.repo.base import BaseRepo


class UserRepo(BaseRepo):
    async def get_or_create_user(
        self,
        telegram_id: int,
        username: Union[str, None],
        full_name: str,
        status: str,
        role: str,
        language: str,
    ):
        """
        Creates or updates a new user in the database and returns the user object.
        :param telegram_id: The user's telegram ID.
        :param username: The user's username. It's an optional parameter.
        :param full_name: The user's full name.
        :param status: The user's status.
        :param role: The user's role.
        :param language: The user's language.
        :return: User object, None if there was an error while making a transaction.
        """

        insert_stmt = (
            insert(User)
            .values(
                telegram_id=telegram_id,
                username=username,
                full_name=full_name,
                status=status,
                role=role,
                language=language,
            )
            .on_conflict_do_update(
                index_elements=[User.telegram_id],
                set_=dict(
                    username=username,
                    full_name=full_name,
                ),
            )
            .returning(User)
        )
        result = await self.session.execute(insert_stmt)

        await self.session.commit()
        return result.scalar_one()
