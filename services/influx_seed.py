import random
from datetime import datetime, timedelta, timezone

# =========================
# IMPORTS FROM MONGO
# =========================
from services.student_information_service import (
    students_col,
    enrollments_col,
    assignments_col
)

# =========================
# IMPORTS FROM INFLUX
# =========================
from services.analytics_service import (
    log_student_login,
    log_student_event_add_course,
    log_student_event_visit_course,
    log_student_event_submit_assignment
)

# =========================
# CONFIGURATION (LOGIC AWARE)
# =========================
DAYS_BACK = 7

LOGIN_RANGE = (3, 8)           # logins per student (per week)
VISITS_PER_COURSE = (3, 12)    # visits per enrolled course
SUBMISSION_RATE = 0.6          # 60% of assignments are submitted


# =========================
# TIME HELPERS
# =========================
def random_time_last_days(days: int) -> datetime:
    """
    Returns a random UTC datetime within the last N days.
    """
    now = datetime.now(timezone.utc)
    delta = timedelta(
        days=random.randint(0, days - 1),
        hours=random.randint(0, 23),
        minutes=random.randint(0, 59),
        seconds=random.randint(0, 59),
    )
    return now - delta


# =========================
# MAIN SEED FUNCTION
# =========================
def seed_influx_activity():
    print("\n📊 Seeding InfluxDB activity (LOGIC-AWARE)...\n")

    # =========================
    # LOAD DATA FROM MONGO
    # =========================
    students = list(students_col.find({}, {"_id": 0}))
    enrollments = list(enrollments_col.find({}, {"_id": 0}))
    assignments = list(assignments_col.find({}, {"_id": 0}))

    # =========================
    # BUILD LOOKUP STRUCTURES
    # =========================
    student_courses = {}
    course_assignments = {}

    for e in enrollments:
        student_courses.setdefault(e["student_id"], []).append(e["course_id"])

    for a in assignments:
        course_assignments.setdefault(a["course_id"], []).append(a["assignment_id"])

    print(f"👨‍🎓 Students loaded     : {len(students)}")
    print(f"🧾 Enrollments loaded  : {len(enrollments)}")
    print(f"📝 Assignments loaded  : {len(assignments)}\n")

    # ==================================================
    # 1) LOGIN EVENTS (PER STUDENT)
    # ==================================================
    print("🔑 Logging student login events...")
    for student in students:
        student_id = student["student_id"]

        login_count = random.randint(*LOGIN_RANGE)
        for _ in range(login_count):
            log_student_login(
                student_id,
                login_time=random_time_last_days(DAYS_BACK)
            )

    # ==================================================
    # 2) ADD COURSE EVENTS (ONCE PER ENROLLMENT)
    # ==================================================
    print("➕ Logging course add events...")
    for student_id, courses in student_courses.items():
        for course_id in courses:
            log_student_event_add_course(
                student_id,
                course_id,
                timestamp=random_time_last_days(DAYS_BACK)
            )

    # ==================================================
    # 3) COURSE VISITS (ONLY FOR ENROLLED COURSES)
    # ==================================================
    print("👀 Logging course visit events...")
    for student_id, courses in student_courses.items():
        for course_id in courses:
            visit_count = random.randint(*VISITS_PER_COURSE)
            for _ in range(visit_count):
                log_student_event_visit_course(
                    student_id,
                    course_id,
                    timestamp=random_time_last_days(DAYS_BACK)
                )

    # ==================================================
    # 4) ASSIGNMENT SUBMISSIONS (REAL ASSIGNMENTS ONLY)
    # ==================================================
    print("📝 Logging assignment submission events...")
    for student_id, courses in student_courses.items():
        for course_id in courses:
            assignments_for_course = course_assignments.get(course_id, [])

            for assignment_id in assignments_for_course:
                if random.random() <= SUBMISSION_RATE:
                    log_student_event_submit_assignment(
                        student_id,
                        course_id,
                        assignment_id,
                        timestamp=random_time_last_days(DAYS_BACK)
                    )

    print("\n✅ InfluxDB activity seeding completed successfully\n")
