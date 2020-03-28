#!/bin/bash
# Benchmarking script for Debian/Ubuntu VPS
# For testing purposes only. Run this on a server you do not intend to keep around.
# Source:
# https://github.com/haydenjames/bench-scripts/blob/c55a3286743587da9c2e924b5a68a1b0c5b7049c/README.md
#

apt install -y -qq wget curl screen

wget -qO- bench.sh | bash 2>&1 | tee -a benchmark.out

(curl -s wget.racing/nench.sh | bash; curl -s wget.racing/nench.sh | bash) 2>&1 | tee -a benchmark.out

bash <(wget --no-check-certificate -O - https://raw.github.com/mgutz/vpsbench/master/vpsbench) 2>&1 | tee -a benchmark.out

wget http://busylog.net/FILES2DW/busytest.sh -O - -o /dev/null | bash 2>&1 | tee -a benchmark.out

wget https://raw.githubusercontent.com/STH-Dev/linux-bench/a180b92/linux-bench.sh && chmod +x linux-bench.sh && ./linux-bench.sh 2>&1 | tee -a benchmark.out

wget https://raw.githubusercontent.com/hidden-refuge/bench-sh-2/702d4f4/bench.sh && chmod +x bench.sh && ./bench.sh 2>&1 | tee -a benchmark.out

#  2>&1 | tee -a benchmark.out
