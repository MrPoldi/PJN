import math
rmse = 0.0
mae = 0.0
num = 0

with open("test.txt", "r", encoding="utf-8") as in_file, open("predictions.txt", "r", encoding="utf-8") as out_file:
    for line_real, line_pred in zip(in_file, out_file):
        real = line_real[:3]
        pred = line_pred.rstrip("\n")
        rmse += (float(pred) - float(real)) ** 2
        mae += abs(float(pred) - float(real))
        num += 1

rmse = rmse / num
rmse = math.sqrt(rmse)

mae = mae/num

print("RMSE: " + str(rmse))
print("MAE: " + str(mae))


# vw -d training.txt -f model.vw -l 0.05 --passes 2 -c  --normalized
# vw -d test.txt -i model.vw -p predictions.txt
