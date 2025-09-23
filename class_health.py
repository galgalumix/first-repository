class Machine:
    """기구 기본 클래스"""
    def __init__(self, name, target_muscle_group, weight_kg):
        self.name = name
        self.target_muscle_group = target_muscle_group    # 기구가 주로 단련하는 근육 그룹
        self.weight_kg = weight_kg                        # 기구의 무게
        self.is_in_use = False
        print(f"{self.name} 기구입니다. 주 타겟 근육은: {self.target_muscle_group}, 기구 무게는 {self.weight_kg}kg")

    def start_use(self):
        """기구 사용"""
        if self.is_in_use:
            print(f"'{self.name}' 기구를 이미 사용 중입니다.")
        else:
            self.is_in_use = True
            print(f"'{self.name}' 기구 사용을 시작합니다.")

    def end_use(self):
        """기구 사용 종료"""
        if not self.is_in_use:
            print(f"'{self.name}' 기구는 현재 사용 중이 아닙니다.")
        else:
            self.is_in_use = False
            print(f"'{self.name}' 기구 사용을 종료합니다.")

    def __str__(self):
        """객체를 문자열로 표현"""
        status = "사용 중" if self.is_in_use else "사용 가능"
        return f"기구: {self.name} | 타겟 근육: {self.target_muscle_group} | 무게: {self.weight_kg} kg | 상태: {status}"


class LatPulldown(Machine):
    """LatPulldown 클래스"""
    def __init__(self, weight_kg):
        super().__init__(name="렛풀다운 머신", target_muscle_group="등", weight_kg=weight_kg)
        self.handle_type = "와이드 그립 바"

    def perform_rep(self):
        print(f"{self.handle_type}를 당깁니다. 등 근육에 집중하세요!")


class ChestPress(Machine):
    """ChestPress 클래스"""
    def __init__(self, weight_kg):
        super().__init__(name="체스트 프레스 머신", target_muscle_group="가슴", weight_kg=weight_kg)
        self.grip_style = "뉴트럴 그립"

    def perform_rep(self):
        print(f"{self.grip_style}으로 앞으로 밀어냅니다. 가슴 근육에 자극이 오네요!")


class LegPress(Machine):
    """LegPress 클래스"""
    def __init__(self, weight_kg):
        super().__init__(name="레그 프레스 머신", target_muscle_group="다리", weight_kg=weight_kg)
        self.foot_placement = "표준 발 너비"

    def perform_rep(self):
        print(f"{self.foot_placement}로 플랫폼을 밀어냅니다. 다리 근육이 타는 느낌이 들어요!")


if __name__ == "__main__":
    # 각 기구 객체 생성 (테스트 코드)
    lat_pulldown = LatPulldown(weight_kg=40)
    chest_press = ChestPress(weight_kg=20)
    leg_press = LegPress(weight_kg=60)

    print("\n--- 현재 기구 상태 ---")
    print(lat_pulldown)
    print(chest_press)
    print(leg_press)

    print("\n--- 기구 사용 시뮬레이션 ---")
    lat_pulldown.start_use()
    lat_pulldown.perform_rep()
    print(lat_pulldown)

    chest_press.start_use()
    chest_press.perform_rep()
    print(chest_press)

    leg_press.start_use()
    leg_press.perform_rep()
    print(leg_press)

    print("\n--- 운동 종료 후 ---")
    lat_pulldown.end_use()
    print(lat_pulldown)

    chest_press.end_use()
    print(chest_press)

    leg_press.end_use()
    print(leg_press)