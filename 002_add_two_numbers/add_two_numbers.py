from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


# Skip SolutionOne to be dry-run or examine!
class SolutionOne:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sum = 0
        carry = 0
        pointer_1: ListNode = l1
        pointer_2: ListNode = l2

        result: list = []

        # Assuming l1 is always a longer list than l2
        while pointer_1 is not None:
            if pointer_2 is not None:
                add = pointer_1.val + pointer_2.val + carry
                if add >= 10:
                    sum = add % 10
                    carry = add // 10
                else:
                    sum = add
                    carry = 0
                pointer_2 = pointer_2.next
            else:
                add = pointer_1.val + carry
                if add >= 10:
                    sum = add % 10
                    carry = add // 10
                else:
                    sum = add
                    carry = 0
            result.append(sum)
            pointer_1 = pointer_1.next

        if carry != 0:
            result.append(carry)

        # [1, 2, 3, 4]
        head = ListNode(result[0])
        current: ListNode = head

        for num in result[1:]:
            new_node = ListNode(num)
            current.next = new_node
            current = new_node

        return head


class SolutionTwo:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sum = 0
        carry = 0
        ptr_1: ListNode = l1
        ptr_2: ListNode = l2

        head = None
        current = None

        while ptr_1 or ptr_2 or carry:
            add = carry

            if ptr_1:
                add += ptr_1.val
                ptr_1 = ptr_1.next
            if ptr_2:
                add += ptr_2.val
                ptr_2 = ptr_2.next

            sum = add % 10
            carry = add // 10

            if head is None:
                head = ListNode(sum)
                current = head
            else:
                current.next = ListNode(sum)
                current = current.next

        return head
