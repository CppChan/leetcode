# public class Solution {
#   public int random7() {
#     int[][]list = new int[5][5];
#     int k = 0;
#     for(int i = 0; i<5; i++){
#       for(int j=0; j<5; j++){
#         list[i][j]=k;
#         k++;
#       }
#     }
#     int x = RandomFive.random5();
#     int y = RandomFive.random5();
#     if(list[x][y]>20)return random7();
#     else if (list[x][y]>=0 && list[x][y]<=6)return list[x][y];
#     else if (list[x][y]>=7 && list[x][y]<=13)return list[x][y]-7;
#     else return list[x][y]-14;
#   }
# }

#
# public
#
#
# class Solution {
# public int random1000() {
# int[][]list = new int[5][625];
# int k = 0;
# for (int i = 0;i < 5;i++){
# for (int j = 0; j < 625;j++){
# list[i][j]=k;
# k++;
# }
# }
# int temp = list[RandomFive.random5()][random125()];
# if (temp > 2999)
#
#
# return random1000();
# else return temp % 1000;
# }
#
# public
# int
# random25()
# {
# int[][]
# list = new
# int[5][5];
# int
# k = 0;
# for (int i = 0; i < 5; i++){
# for (int j=0; j < 5; j++){
# list[i][j]=k;
# k++;
# }
# }
# int
# x = RandomFive.random5();
# int
# y = RandomFive.random5();
# return list[x][y];
# }
# public
# int
# random125()
# {
# int[][]
# list = new
# int[25][25];
# int
# k = 0;
# for (int i = 0; i < 25; i++){
# for (int j=0; j < 25; j++){
# list[i][j]=k;
# k++;
# }
# }
# int
# x = random25();
# int
# y = random25();
# return list[x][y];
# }
# }
