from models.constant import Constant
from seed.define_constants import (
    EXPERIENCE_TYPES,
    EXPERIENCE_TYPES_PREFIX,
    LANGUAGES,
    LANGUAGES_PREFIX,
    NOTIFICATIONS,
    NOTIFICATIONS_PREFIX,
    POSITIONS,
    POSITIONS_PREFIX,
    SKILLS,
    SKILLS_PREFIX,
    SYSTEM_ROLES,
)
from utils import get_instance, log_prefix

_, db = get_instance()


def common_constants(type, prefix: str):
    for idx, name in enumerate(type):
        constant = Constant(constant_name=name, prefix=prefix, index=idx)
        db.session.add(constant)


def constant_seeder():
    try:
        log_prefix(__file__, "Start seeding Constants...")
        for idx, (name, prefix) in enumerate(SYSTEM_ROLES):
            constant = Constant(constant_name=name, prefix=prefix, index=idx)
            db.session.add(constant)

        common_constants(EXPERIENCE_TYPES, EXPERIENCE_TYPES_PREFIX)
        common_constants(POSITIONS, POSITIONS_PREFIX)
        common_constants(SKILLS, SKILLS_PREFIX)
        common_constants(NOTIFICATIONS, NOTIFICATIONS_PREFIX)

        for idx, language in enumerate(LANGUAGES):
            constant = Constant(
                constant_name=language["name"],
                prefix=LANGUAGES_PREFIX,
                index=idx,
                note=language["note"],
            )
            db.session.add(constant)

        db.session.commit()
        log_prefix(__file__, "Finished seeding Constants.")
    except Exception as error:
        db.session.rollback()
        log_prefix(__file__, error, type="error")
