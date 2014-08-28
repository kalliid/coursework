echo "echo Unpacking file $1"
echo "cat > $1 <<EOF"
cat $1
echo "  "
echo "EOF"