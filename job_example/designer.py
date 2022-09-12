from job import Job


class Designer(Job):
    def do(self) -> None:
        print(f"디자인 관련 업무를 합니다.")
