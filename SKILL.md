---
name: dieu_google_flow_video_prompting
description: Chuyển kịch bản, asset, phong cách, brief hoặc dữ liệu hỗn hợp thành bộ prompt copy-ready cho Google Flow; ưu tiên tuyệt đối tính nhất quán nhân vật, bối cảnh, đạo cụ, hình ảnh, âm thanh và continuity xuyên nhiều clip.
version: 2.0.1
metadata:
  hermes:
    tags: [dieu, google-flow, veo, gemini-omni, video-prompting, continuity, character-consistency, scene-consistency]
---

# Dieu Google Flow Video Prompting

## Mục tiêu

Nhận bất kỳ dữ liệu đầu vào nào Sếp cung cấp—kịch bản, voice-over, ảnh, video, moodboard, character sheet, sản phẩm, phong cách, shot list hoặc brief thô—và chuyển thành prompt hoặc bộ prompt có thể copy trực tiếp vào Google Flow.

Đây là skill **creative direction + continuity + Flow prompting**, không phải skill tích hợp API. Không đưa code, JSON, API schema hoặc tham số developer vào output trừ khi Sếp yêu cầu rõ.

## Nguyên tắc tối cao: continuity-first

Trước khi viết prompt, phải tạo **Continuity Bible**. Không được viết từng shot độc lập rồi hy vọng model tự giữ nhất quán.

Các lớp phải khóa khi liên quan:
1. **Character identity**: khuôn mặt, tuổi hình ảnh, tóc, vóc dáng, da, dấu hiệu nhận diện.
2. **Wardrobe**: từng món đồ, màu, chất liệu, tình trạng, phụ kiện.
3. **Performance**: tính cách, body language, trạng thái cảm xúc kế thừa.
4. **Environment**: kiến trúc, layout, vật liệu, thời điểm, thời tiết, vật thể nền.
5. **Props/product**: hình dáng, màu, chất liệu, tay cầm, vị trí và trạng thái.
6. **Cinematography**: aspect ratio, lens family, camera height, screen direction, axis, movement language.
7. **Look**: lighting direction, color palette, contrast, texture, visual medium.
8. **Audio**: giọng nói, accent, ambience, recurring sound motif.
9. **Temporal state**: shot trước kết thúc ở đâu; shot sau bắt đầu từ trạng thái nào.

### Thứ tự ưu tiên khi có xung đột

`Asset đã duyệt > dữ kiện Sếp khóa > kịch bản > Continuity Bible > lựa chọn sáng tạo mới`

Không được tự ý thay đổi dữ kiện ở tầng cao hơn. Nếu hai asset đã duyệt mâu thuẫn, phải báo Sếp hoặc đề xuất chọn một asset master.

## Quy trình bắt buộc

### 1. Kiểm kê đầu vào

Phân loại:
- **Immutable facts**: không được đổi.
- **Creative freedom**: được phép đề xuất.
- **Missing information**: có thể dùng giả định hợp lý và ghi rõ.
- **Conflicts**: phải giải quyết trước prompt.
- **Assets**: gán đúng vai trò, không coi mọi ảnh như nhau.

Vai trò asset:
- `identity_reference`
- `wardrobe_reference`
- `product_reference`
- `environment_reference`
- `style_reference`
- `start_frame`
- `end_frame`
- `motion_reference`

Một asset có thể có nhiều vai trò, nhưng phải nói rõ phần nào cần lấy và phần nào không lấy.

### 2. Tạo Continuity Bible

Dùng schema trong `assets/continuity-bible.yaml` và hướng dẫn tại `references/continuity-system.md`.

Mỗi trường gắn một mức khóa:
- **HARD**: không được đổi giữa các shot.
- **SOFT**: có thể thay đổi nếu phục vụ diễn biến.
- **FREE**: model được phép sáng tạo.

Nếu chỉ tạo một shot đơn, vẫn phải có continuity mini-card cho subject, environment và look.

### 3. Chia kịch bản theo visual beat

Không chia máy móc theo câu. Mỗi clip nên có:
- một mục tiêu thị giác;
- một trạng thái mở đầu;
- một hành động trung tâm;
- một trạng thái kết thúc;
- một camera logic;
- một nhịp cảm xúc;
- một nhiệm vụ âm thanh.

Nếu quá tải so với thời lượng, chia thành nhiều clip. Xem `references/script-to-shot-and-feasibility.md`.

### 4. Chọn workflow Flow

- **Text-to-video**: không có asset bắt buộc.
- **Image-to-video**: một ảnh đã khóa identity/composition; prompt tập trung motion.
- **Multi-reference/ingredients**: nhiều asset khóa character/product/environment/style.
- **First + last frame**: khóa trạng thái đầu/cuối; prompt mô tả đường chuyển tiếp.
- **Continuous single shot**: một beat, một camera logic.
- **Timestamp sequence**: nhiều beat trong cùng clip và thật sự cần nhiều shot.
- **Multiple clips**: kịch bản dài hoặc cần kiểm soát continuity tốt hơn.
- **Revision after generation**: sửa theo delta, giữ phần đang tốt.

Không chọn workflow dựa trên API. Chọn theo mức kiểm soát sáng tạo và asset có sẵn trong Flow.

### 5. Viết prompt

Công thức nền:

`[Cinematography] + [Subject] + [Action] + [Context] + [Style & Ambiance] + [Audio] + [End state]`

Ba lớp motion:
- subject motion;
- camera motion;
- environmental motion.

Prompt phải ưu tiên chronology và khả năng quay hơn mỹ từ. Mỗi cụm từ phải có chức năng điều khiển.

### 6. Gắn continuity vào từng clip

Không lặp toàn bộ bible. Với mỗi clip, tạo:
- **Global locks**: identity/look/location anchors cần lặp.
- **Inherited state**: trạng thái nhận từ clip trước.
- **Shot-specific action**: điều mới diễn ra.
- **End-state handoff**: trạng thái bàn giao cho clip sau.

Mỗi clip phải có continuity ID, ví dụ `CHAR_A`, `LOC_01`, `PROP_PHONE_01`, tránh các mô tả thay đổi tên tùy ý.

### 7. QA và hard fail

Dùng `references/flow-qa-hard-fails.md`. Không bàn giao nếu:
- nhân vật/bối cảnh/đạo cụ mâu thuẫn asset hoặc clip trước;
- thiếu state handoff giữa các clip liên tục;
- thay lens, lighting direction, weather hoặc screen direction không có lý do kể chuyện;
- camera instruction mâu thuẫn;
- action/dialogue quá tải duration;
- timestamp không khớp;
- asset quan trọng chưa được phân vai;
- prompt sửa lỗi không nêu `Preserve` và `Change`;
- output lẫn code/API không được yêu cầu.

## Continuity strategy theo loại dự án

### Một nhân vật qua nhiều clip
- Chọn 1–3 ảnh master rõ mặt, tóc, vóc dáng và wardrobe.
- Viết identity anchor ngắn, bất biến, dùng đúng từ ở mọi prompt.
- Khóa wardrobe theo scene; nếu thay đồ phải có transition/story reason.
- Giữ voice profile và body-language signature.
- Không thêm đặc điểm ngoại hình mới ở clip sau.

### Một bối cảnh qua nhiều góc máy
- Tạo environment map: layout, cửa, cửa sổ, vật liệu, props lớn, nguồn sáng.
- Khóa time of day, weather, light direction và palette.
- Nêu vị trí tương đối của character/props khi đổi góc.
- Theo dõi screen direction và 180-degree axis; chỉ phá trục có chủ đích.

### Sản phẩm/đạo cụ
- Khóa hình dáng, màu, chất liệu, tỷ lệ, orientation và tay đang cầm.
- Theo dõi trạng thái: đóng/mở, sạch/bẩn, đầy/vơi, nguyên/vỡ.
- Chữ/logo chính xác cần cảnh báo kiểm tra hoặc hậu kỳ.

### Chuỗi hành động
- Clip N kết thúc ở pose/location/state nào thì clip N+1 phải mở từ đó.
- Nếu không thể dùng đúng end frame làm start frame, lặp lại state bằng mô tả và reference phù hợp.
- Không teleport nhân vật, đổi tay cầm đồ hoặc đổi hướng di chuyển ngoài ý muốn.

## Prompt modes

### Generate prompt
Mô tả đầy đủ shot mới.

### Animate-asset prompt
Không mô tả lại ảnh quá mức; tập trung motion, camera, environment, audio và end state.

### Revision prompt

```text
Preserve: [mọi phần đang đúng].
Change only: [một hoặc vài lỗi cụ thể].
Continuity locks: [identity/location/prop/look anchors].
Do not alter: [các thành phần dễ drift].
Desired timing and motion: [delta cụ thể].
```

## Output mặc định cho Sếp

### Quy cách trình bày prompt — bắt buộc

- **Mỗi prompt là đúng một đoạn văn liền mạch**; không chia nội dung của một prompt thành bullet, danh sách, bảng, tiêu đề con hoặc nhiều đoạn.
- **Nếu có từ hai prompt trở lên, giữa hai prompt liên tiếp phải có đúng một dòng trắng**; không đặt bullet, dấu phân cách, tiêu đề, nhãn quản trị hoặc nội dung khác chen giữa các prompt trong khối prompt copy-ready.
- Hai quy tắc trên chỉ thay đổi hình thức trình bày của phần **Prompt copy-ready**. **Tất cả nội dung, cấu trúc quản trị, continuity, workflow, asset map, thiết lập, end-state handoff, rủi ro và các nguyên tắc khác của skill phải giữ nguyên.**
- Các nhãn quản trị như `Clip ID`, `Inherited state`, `Assets`, `Continuity locks`, `End-state handoff` và `Rủi ro` vẫn được đặt ngoài khối prompt copy-ready theo cấu trúc mặc định.
- Trước khi bàn giao, phải QA định dạng: xác nhận mỗi prompt chỉ có một đoạn và các prompt cách nhau đúng một dòng trắng.

1. **Workflow đề xuất** + lý do.
2. **Input/asset map**.
3. **Continuity locks**: character, environment, props, look, audio.
4. **Prompt copy-ready cho Flow**.
5. **Negative prompt** nếu workflow/giao diện có trường phù hợp.
6. **Thiết lập đề xuất**: aspect ratio, duration, audio, asset assignment.
7. **End-state handoff** nếu có clip tiếp theo.
8. **Rủi ro và phương án sửa**.

Với kịch bản nhiều clip, output cho từng clip:

```text
Clip ID / mục tiêu
Inherited state
Assets dùng trong Flow
Continuity locks
Prompt copy-ready
End-state handoff
Rủi ro
```

Không bắt Sếp đọc YAML nội bộ trừ khi Sếp yêu cầu production bible đầy đủ.

## Đóng gói skill thành website

Khi xây website nhận kịch bản và ảnh tham chiếu để tạo prompt, áp dụng kiến trúc, input/output contract, bảo mật, UX và verification gates trong `references/web-app-wrapper-pattern.md`. Phải phân biệt rõ demo template với AI dùng skill thật; preload skill đích một cách tường minh, và không được coi metadata file là đã phân tích nội dung ảnh.

## Nguồn và kiến thức model

Fact Google được lưu tại `references/google-official-notes.md`. Omni/Veo API notes chỉ là tài liệu tùy chọn tại `references/optional-api-notes.md`, không thuộc luồng Flow mặc định.

## Học từ kết quả Flow

Khi Sếp gửi video/screenshot/nhận xét sau render:
1. So sánh với intent và continuity locks.
2. Gắn failure tag từ `references/failure-taxonomy.md`.
3. Phân biệt lỗi prompt, asset conflict, overload hay model variance.
4. Viết revision theo delta; không phá phần đang tốt.
5. Chỉ bổ sung bài học vào skill khi cách sửa đã được kết quả thực tế xác nhận hoặc lặp lại nhiều lần.
