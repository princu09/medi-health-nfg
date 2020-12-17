$(".addRow").click(function () {
    console.log("Success")
    $(".add--item--btn").before(addItem)
})


addItem = `<tr class="item-row">
    <td class="justify-conent-space-between align-items-center d-flex">
    <a id="delete" class="delete mr-3" href="javascript:;" title="Remove Item"><i class="fas fa-times"></i></a>
    <input class="bill--item" type="text"></td>
    <td class="text-center"><input class="bill--batch" type="text"></td>
    <td class="text-center"><input class="bill--exp" type="text"></td>
    <td class="text-center"><input class="bill--qty" type="text"></td>
    <td class="text-center"><input class="bill--pack" type="text"></td>
    <td class="text-center"><input class="bill--mrp" type="text"></td>
    <td class="text-center"><input class="bill--rate" type="text"></td>
    <td class="text-center"><input class="bill--cgst" type="text"></td>
    <td class="text-center"><input class="bill--sgst" type="text"></td>
    <td class="text-center"><input class="bill--shedule" type="text"></td>
    <td class="text-right">$980.00</td>
</tr>`