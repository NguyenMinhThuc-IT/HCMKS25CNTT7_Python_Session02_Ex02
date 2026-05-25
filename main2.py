donor_age = int(input(
    "Nhập tuổi người hiến máu: "
))

donor_weight = float(input(
    "Nhập cân nặng người hiến máu (kg): "
))

print("\n========== KẾT QUẢ KIỂM TRA ==========")

if donor_age >= 18 and donor_weight >= 50:
    print("ĐỦ ĐIỀU KIỆN HIẾN MÁU")

else:
    print("KHÔNG ĐỦ ĐIỀU KIỆN")

    if donor_age < 18:
        print("- Lý do: Chưa đủ 18 tuổi")

    if donor_weight < 50:
        print("- Lý do: Cân nặng dưới 50kg")

print("======================================")