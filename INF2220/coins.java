class Coins {
    int[] coins;

    Coins(int[] possible_coins) {
        coins = possible_coins;
    }

    int numOfCoins(int amount) {
        int n = 0;

        for (int coin : coins) {
            while (amount > coin) {
                System.out.println(coin);
                amount -= coin;
                n++;
            }
        }

        return n;
    }

    public static void main(String[] args) {
        int[] coins = {50, 20, 10, 5, 2, 1};
        Coins test = new Coins(coins);
        System.out.println(test.numOfCoins(72));
    }
}
